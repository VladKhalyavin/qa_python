# qa_python
### Перед запуском тестов:
Установить pytest

```bash
pip install pytest
```

### Запускать тесты командой:
```bash
pytest -v tests.py
```

### Список тестов:
1. *test_books_collection_true* - проверка экземпляра класса BooksCollector на наличие и состав атрибутов
2. *test_add_new_book_valid_boundary_conditions_book_added* - проверка валидных граничных значений add_new_book - книга добавлена
3. *test_add_new_book_invalid_boundary_conditions_book_not_added* - проверка невалидных граничных значений add_new_book - книга не добавлена
4. *test_set_book_genre_from_genre_genre_added* - проверка добавления жанра из списка genre - книге присвоен жанр
5. *test_set_book_genre_not_in_genre_genre_not_added* - проверка проверка добавления жанра не состоящего в списке genre - жанр книги не изменился
6. *test_set_book_name_not_in_books_genre_genre_not_added* - проверка добавления жанра книге, отсутствующей в books_genre - books_genre не изменился
7. *test_get_books_with_specific_genre_books_collection_received_three_horrors* - проверка списка книг заданного жанра - получен список книг заданного жанра
8. *test_get_books_for_children_books_collection_received_only_children_genres* - проверка получения списка книг для детей - возвращены только фильмы с детскими жанрами
9. *test_add_book_in_favorites_name_not_in_favorites_book_added* - проверка добавления книги в избранное, книга не находится в избранном - успешное добавление в избранное
10. *test_add_book_in_favorites_name_in_favorites_book_not_added* - проверка повторного добавления книги в избранное - книга добавлена в список только один раз
11. *test_delete_book_from_favorites_name_in_favorites_book_deleted* - проверка удаления книги из избарнного - удаляется одна из двух книг