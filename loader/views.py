# Импортируем фреймворк Flask и другие его модули
from flask import Blueprint, render_template, request
# Импортируем модуль логирования logging
import logging
# Импортируем исключение JSONDecodeError из модуля json
from json import JSONDecodeError
# Импортируем написанные функции для дальнейшей работы с ними
from functions import add_post
from loader.utils import save_picture
# Создаём модуль блюпринт loader_blueprint
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post', methods=['GET'])
def post_page():
    """Вывод страницы добавления поста"""
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def add_post_page():
    """Добавление поста"""
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return 'Нет картинки или текста'
    if picture.filename.split(".")[-1] not in ["jpeg", "jpg", "png", "svg", "gif"]:
        logging.info('Загруженный файл не картинка')
        return "Неверное расширение файла"
    try:
        picture_path: str = '/' + save_picture(picture)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return "Файл не найден"
    except JSONDecodeError:
        return "Невалидный файл"
    post: dict = add_post({'pic': picture_path, 'content': content})

    return render_template('post_uploaded.html', post=post)