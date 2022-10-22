# Импортируем стандартный модуль JSON
import json


def load_posts() -> list[dict]:
    """
    Чтение данных из JSON файла
    """
    with open('posts.json', 'r', encoding='utf=8') as file:
        data = json.load(file)
        return data


def get_posts_by_word(word: str) -> list[dict]:
    """
    Функция, которая возвращает пост по слову (подстроке)
    """
    result = []
    for post in load_posts():
        if word.lower() in post['content'].lower():
            result.append(post)
    return result


def add_post(post: dict) -> dict:
    """
    Добавление поста с записью в JSON файл
    """
    posts: list[dict] = load_posts()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file, ensure_ascii=False)
    return post
