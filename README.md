# qa_python
def test_add_new_book_add_two_books(self)  - Проверяем, что добавилось именно две книги
def test_add_new_book_already_exists(self) - Проверяем, что добавление дублирующей книги не приведет к созданию нескольких записей
def test_add_new_book_empty_name(self) - Проверям, что книга без названия не добавлена
def test_add_new_book_long_name(self) - Проверяем, что книга с название больше 40 символом не добавлена в список
def test_set_book_genre_success(self) - Проверяем, что жанр может быть успешно присвоен книге, если и книга, и жанр соответствуют требованиям.
def test_set_book_genre_invalid_genre(self) - Проверяем, что книге не будет присвоены несуществующий жанр.
def test_set_book_genre_book_not_exists(self - Проверяем, что попытка определить жанр несуществующей книги ни к чему не приведёт.
def test_get_book_genre_success(self) - Проверям, что для существующей книги будет возвращен правильный жанр.
def test_get_book_genre_book_not_exists(self) -Проверяем, что  возвращает значение None для книги, которая не была добавлена в коллекцию.
def test_get_books_for_children_success(self - Проверяем, что книги определенного жанра будут правильно отфильтрованы и возвращены.
def test_add_book_in_favorites_success(self) - Проверям успешное добавление книги в избранное
def test_add_book_in_favorites_already_in_favorites(self) - Проверяем, что существующую книгу в изрбанном нельзя добавить
def test_delete_book_from_favorites_success(self): - Проверка удаления книги из избранного
def test_delete_book_from_favorites_nonexistent_book(self): - Провереям, что метод delete_book_from_favorites корректно работает, когда книга, которую нужно удалить из избранного, отсутствует в списке избранного.
def test_get_list_of_favorites_books_success(self) - Проверям чтоо при наличии книг в избранном, метод возвращается правильный список книг.
def test_get_list_of_favorites_books_empty(self): - Проверяем, что метод вернет пустой список, если в избранное ничего не добавлено
@pytest.mark.parametrize создали параметры  с наванием книги, жанром, и присваемым жанром.
def test_set_book_genre_parametrized(self, book_name, genre, unknown_genre) -  параметризованный тест проверяет, что установка жанра работает корректно для различных книг и жанров.
 
