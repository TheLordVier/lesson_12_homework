# Импортируем фреймворк Flask и другие его модули
from flask import Blueprint, render_template, request
# Импортируем модуль логирования logging
import logging
# Импортируем исключение JSONDecodeError из модуля json
from json import JSONDecodeError
# Импортируем написанные функции для дальнейшей работы с ними
from functions import get_posts_by_word
# Создаём модуль блюпринт main_blueprint
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route("/")
def main_page():
    """Главная страница"""
    return render_template("index.html")


@main_blueprint.route("/search/")
def search_page():
    """Поиск и вывод поста по слову или подстроке"""
    search_query = request.args.get('s', '')
    logging.info('Выполняю поиск')
    try:
        posts = get_posts_by_word(search_query)
    except FileNotFoundError:
        logging.error('Файл не найден')
        return "Файл не найден"
    except JSONDecodeError:
        return "Невалидный файл"
    return render_template("post_list.html", query=search_query, posts=posts)



