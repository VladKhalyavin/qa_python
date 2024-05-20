import pytest
import random
from main import BooksCollector

BOOKS_COLLECTION = {
    'Дракула': 'Ужасы',
    'Оно': 'Ужасы',
    'Сияние': 'Ужасы',
    'Лунный камень': 'Детективы',
    'Дюна': 'Фантастика',
    'Солярис': 'Фантастика',
}


@pytest.fixture(scope='function')
def collection():
    """
    Создает экземпляр класса BooksCollector
    """
    collection = BooksCollector()
    return collection


@pytest.fixture(scope='function')
def book_without_genre(collection):
    """
    Добавляет в books_genre книгу с случайным имененм без жанра
    """
    book_without_genre = random.choice(list(BOOKS_COLLECTION.keys()))
    collection.add_new_book(book_without_genre)
    return book_without_genre


@pytest.fixture(scope='function')
def books_collection(collection):
    """
    Создает коллекцию книг по жанрам
    """
    for key, value in BOOKS_COLLECTION.items():
        collection.add_new_book(key)
        collection.set_book_genre(key, value)
    return BOOKS_COLLECTION


@pytest.fixture(scope='function')
def favorites_books(collection):
    """
    Добавляет в список favorites две книги с случайными именими
    """
    favorites_books = [random.choice(list(BOOKS_COLLECTION.keys())), random.choice(list(BOOKS_COLLECTION.keys()))]
    while favorites_books[0] == favorites_books[1]:
        favorites_books[1] = random.choice(list(BOOKS_COLLECTION.keys()))

    for i in favorites_books:
        collection.add_new_book(i)
        collection.add_book_in_favorites(i)

    return favorites_books
