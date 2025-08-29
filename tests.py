from main import BooksCollector

import pytest

class TestBooksCollector:
    
    @pytest.fixture
    def book_collector(self):
        return BooksCollector()
    
    @pytest.fixture
    def collector_with_books(self, book_collector):
        book_collector.add_new_book('Лонгольеры')
        book_collector.add_new_book('Убийство в Восточном экспрессе')
        return book_collector

    def test_add_new_book_empty_dict_two_books_added(self, collector_with_books):
        assert len(collector_with_books.books_genre) == 2

    @pytest.mark.parametrize('name, genre', [['Лонгольеры', 'Фантастика'], ['Убийство в Восточном экспрессе', 'Детективы']])
    def test_set_book_genre_dict_without_genre_full_dict(self, collector_with_books, name, genre):
        collector_with_books.set_book_genre(name, genre)
        assert collector_with_books.books_genre[name] == genre
    
    def test_get_books_genre_books_dict_books_genre(self, collector_with_books):
                assert collector_with_books.books_genre.get('Лонгольеры') == ''

    def test_get_books_with_specific_genre_empty_list_books_list_with_specific_genre(self, collector_with_books):
        collector_with_books.set_book_genre('Лонгольеры', 'Фантастика')
        collector_with_books.set_book_genre('Убийство в Восточном экспрессе', 'Детективы')
        assert collector_with_books.get_books_with_specific_genre('Фантастика') == ['Лонгольеры']
    
    def test_get_books_genre_empty_dict_dict_with_two_books(self, collector_with_books):
        expected = {"Лонгольеры": "", "Убийство в Восточном экспрессе": ""}
        assert collector_with_books.get_books_genre() == expected
    
    def test_get_books_for_children_empty_list_books_for_children(self, collector_with_books):
        collector_with_books.set_book_genre('Лонгольеры', 'Фантастика')
        collector_with_books.set_book_genre('Убийство в Восточном экспрессе', 'Детективы')
        assert collector_with_books.get_books_for_children() == ['Лонгольеры']
    
    def test_add_book_in_favorites_empty_list_add_book_to_favorites_list(self, collector_with_books):
        collector_with_books.add_book_in_favorites('Лонгольеры')
        assert 'Лонгольеры' in collector_with_books.get_list_of_favorites_books()
    
    def test_delete_book_from_favorites_list_of_favorites_books_delete_book(self, collector_with_books):
        collector_with_books.add_book_in_favorites('Лонгольеры')
        collector_with_books.delete_book_from_favorites('Лонгольеры')
        assert 'Лонгольеры' not in collector_with_books.get_list_of_favorites_books()
    
    def test_get_list_of_favorites_books_favorites_books_list_get_favorites_list(self, collector_with_books):
        collector_with_books.add_book_in_favorites('Лонгольеры')
        assert collector_with_books.get_list_of_favorites_books() == ['Лонгольеры']
