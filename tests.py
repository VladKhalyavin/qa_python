import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_books_collection_true(self, collection):
        """
        Проверка экземпляра класса BooksCollector на наличие и состав атрибутов
        """
        assert (collection.books_genre == {} and
                collection.favorites == [] and
                collection.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'] and
                collection.genre_age_rating == ['Ужасы', 'Детективы'])

    @pytest.mark.parametrize('name', ['G', 'Ma quande lingues coalesce, li grammatic'])
    def test_add_new_book_valid_boundary_conditions_book_added(self, collection, name):
        """
        add_new_book \n
        Проверка валидных граничных значений add_new_book - книга добавлена
        """
        collection.add_new_book(name)
        assert (len(collection.books_genre) == 1 and
                name in collection.books_genre.keys() and
                '' in collection.books_genre.values())

    @pytest.mark.parametrize('name', ['', 'Ma quande lingues coalesce, li grammatica'])
    def test_add_new_book_invalid_boundary_conditions_book_not_added(self, collection, name):
        """
        add_new_book \n
        Проверка невалидных граничных значений add_new_book - книга не добавлена
        """
        collection.add_new_book(name)
        assert len(collection.books_genre) == 0

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_from_genre_genre_added(self, collection, book_without_genre, genre):
        """
        set_book_genre \n
        Проверка добавления жанра из списка genre - книге присвоен жанр
        """
        collection.set_book_genre(book_without_genre, genre)
        assert genre == collection.books_genre.get(book_without_genre)

    def test_set_book_genre_not_in_genre_genre_not_added(self, collection, book_without_genre):
        """
        set_book_genre \n
        Проверка проверка добавления жанра не состоящего в списке genre - жанр книги не изменился
        """
        genre = 'Триллер'
        collection.set_book_genre(book_without_genre, genre)
        assert collection.books_genre.get(book_without_genre) == ''

    def test_set_book_name_not_in_books_genre_genre_not_added(self, collection):
        """
        set_book_genre \n
        Проверка добавления жанра книге, отсутствующей в books_genre - books_genre не изменился
        """
        genre = 'Фантастика'
        added_book = 'Хоббит'
        unknown_book = 'Скотный двор'

        collection.add_new_book(added_book)
        collection.set_book_genre(unknown_book, genre)
        assert collection.books_genre == {'Хоббит': ''}

    def test_get_book_genre_name_in_books_genre_get_book_genre(self, collection, book_without_genre):
        """
        get_book_genre \n
        Проверка получения жанра книги - получен жанр книги
        """
        genre = 'Детективы'
        collection.set_book_genre(book_without_genre, genre)
        assert collection.get_book_genre(book_without_genre) == genre

    def test_get_books_with_specific_genre_books_collection_received_three_horrors(self, collection, books_collection):
        """
        get_books_with_specific_genre \n
        Проверка списка книг заданного жанра - получен список книг заданного жанра
        """
        assert collection.get_books_with_specific_genre('Ужасы') == ['Дракула', 'Оно', 'Сияние']

    def test_get_books_genre_true(self, collection, books_collection):
        """
        get_books_genre \n
        Проверка получения словаря books_genre - получен словарь books_genre
        """
        assert collection.get_books_genre() == books_collection

    def test_get_books_for_children_books_collection_received_only_children_genres(self, collection, books_collection):
        """
        get_books_for_children_books \n
        Проверка получения списка книг для детей - возвращены только фильмы с детскими жанрами
        """
        assert collection.get_books_for_children() == ['Дюна', 'Солярис']

    def test_add_book_in_favorites_name_not_in_favorites_book_added(self, collection, book_without_genre):
        """
        add_book_in_favorites \n
        Проверка добавления книги в избранное, книга не находится в избранном - успешное добавление в избранное
        """
        collection.add_book_in_favorites(book_without_genre)
        assert len(collection.favorites) == 1 and book_without_genre in collection.favorites

    def test_add_book_in_favorites_name_in_favorites_book_not_added(self, collection, book_without_genre):
        """
        add_book_in_favorites \n
        Проверка повторного добавления книги в избранное - книга добавлена в список только один раз
        """
        collection.add_book_in_favorites(book_without_genre)
        collection.add_book_in_favorites(book_without_genre)
        assert len(collection.favorites) == 1 and book_without_genre in collection.favorites

    def test_delete_book_from_favorites_name_in_favorites_book_deleted(self, collection, favorites_books):
        """
        delete_book_from_favorites \n
        Проверка удаления книги из избарнного - удаляется одна из двух книг
        """
        collection.delete_book_from_favorites(favorites_books[0])
        assert len(collection.favorites) == 1 and favorites_books[1] in collection.favorites

    def test_get_list_of_favorites_books_true(self, collection, favorites_books):
        """
        get_list_of_favorites \n
        Проверка получения списка избарнных книг - получен список избранных книг
        """
        assert collection.get_list_of_favorites_books() == favorites_books
