# Импортируем фреймворк Flask и другие его модули
from flask import Flask, send_from_directory
# Импортируем модуль логирования logging
import logging
# Импортируем используемые блюпринты
from main.views import main_blueprint
from loader.views import loader_blueprint

# Указываем пути выгрузки и загрузки данных
POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

# Инициализируем приложение
app = Flask(__name__)

# Регистрируем блюпринты
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

# Задаём уровень логирования INFO для всего проекта
logging.basicConfig(filename="basic.log", level=logging.INFO)


@app.route("/uploads/<path:path>")
def static_dir(path):
    """"Загрузка(отправка) добавленных картинок по пути: uploads/images"""
    return send_from_directory("uploads", path)


# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)
