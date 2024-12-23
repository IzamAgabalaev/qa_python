import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_already_exists(self):
        collector = BooksCollector()
        collector.add_new_book("Песнь льда и пламяни")
        collector.add_new_book("Песнь льда и пламяни")
        assert len(collector.books_genre) == 1

    def test_add_new_book_empty_name(self):
        collector = BooksCollector()
        collector.add_new_book("")
        assert "" not in collector.books_genre

    def test_add_new_book_long_name(self):
        collector = BooksCollector()
        long_name = "g" * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.books_genre

    def test_set_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book("Песнь льда и пламяни")
        collector.set_book_genre("Песнь льда и пламяни", "Фантастика")
        assert collector.books_genre["Песнь льда и пламяни"] == "Фантастика"

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Песнь льда и пламяни")
        collector.set_book_genre("Песнь льда и пламяни", "Мистика")
        assert collector.books_genre["Песнь льда и пламяни"] == ""

    def test_set_book_genre_book_not_exists(self):
        collector = BooksCollector()
        collector.set_book_genre("Преступление и наказание", "Ужасы")
        assert "Преступление и наказание" not in collector.books_genre

    def test_get_book_genre_success(self):
        collector = BooksCollector()
        collector.add_new_book("Песнь льда и пламяни")
        collector.set_book_genre("Песнь льда и пламяни", "Фантастика")
        genre = collector.get_book_genre("Песнь льда и пламяни")
        assert genre == "Фантастика"

    def test_get_book_genre_book_not_exists(self):
        collector = BooksCollector()
        genre = collector.get_book_genre("Преступление и наказание")
        assert genre is None

    def test_get_books_for_children_success(self):
        collector = BooksCollector()
        collector.add_new_book("Как приручить дракона")
        collector.add_new_book("Астрал")
        collector.set_book_genre("Как приручить дракона", "Мультфильмы")
        collector.set_book_genre("Астрал", "Ужасы")
        result = collector.get_books_for_children()
        assert result == ["Как приручить дракона"]

    def test_add_book_in_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book("Песнь льда и пламяни")
        collector.add_book_in_favorites("Песнь льда и пламяни")
        assert "Песнь льда и пламяни" in collector.favorites

    def test_add_book_in_favorites_already_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Песнь льда и пламяни")
        collector.add_book_in_favorites("Песнь льда и пламяни")
        collector.add_book_in_favorites("Песнь льда и пламяни")
        assert collector.favorites.count("Песнь льда и пламяни") == 1

    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()
        collector.add_new_book("Песнь льда и пламяни")
        collector.add_book_in_favorites("Песнь льда и пламяни")
        collector.delete_book_from_favorites("Песнь льда и пламяни")
        assert "Песнь льда и пламяни" not in collector.favorites

    def test_delete_book_from_favorites_nonexistent_book(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites("Книга1")
        assert "Книга1" not in collector.favorites

    def test_get_list_of_favorites_books_success(self):
        collector = BooksCollector()
        collector.add_new_book("Песнь льда и пламяни")
        collector.add_new_book("Мертвые души")
        collector.add_book_in_favorites("Песнь льда и пламяни")
        collector.add_book_in_favorites("Мертвые души")
        result = collector.get_list_of_favorites_books()
        assert result == ["Песнь льда и пламяни", "Мертвые души"]

    def test_get_list_of_favorites_books_empty(self):
        collector = BooksCollector()
        result = collector.get_list_of_favorites_books()
        assert result == []

    @pytest.mark.parametrize("book_name,genre,unknown_genre", [
        ("Книга1", "Фантастика", "Фантастика"),
        ("Книга2", "Ужасы", "Ужасы"),
        ("Книга3", "Детективы", "Детективы"),
        ("Книга4", "Неизвестный жанр", "")
    ])
    def test_set_book_genre_parametrized(self, book_name, genre, unknown_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == unknown_genre
