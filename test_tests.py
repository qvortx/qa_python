import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_book_to_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')

        assert 'Гордость и предубеждение' in collector.get_books_genre()

    @pytest.mark.parametrize('book', [
        'Гордость и предубеждение',
        'Война и мир',
        'Мастер и Маргарита'
    ])
    def test_add_new_book_add_different_books(self, book):
        collector = BooksCollector()

        collector.add_new_book(book)

        assert book in collector.get_books_genre()

    @pytest.mark.parametrize('genre', [
        'Фантастика',
        'Ужасы',
        'Детективы',
        'Мультфильмы',
        'Комедии'
    ])
    def test_set_book_genre_set_valid_genre(self, genre):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', genre)

        assert collector.get_book_genre('Гордость и предубеждение') == genre

    def test_get_book_genre_return_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')

        assert collector.get_book_genre('Гордость и предубеждение') == 'Фантастика'

    def test_get_books_with_specific_genre_return_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Война и мир')
        collector.add_new_book('Мастер и Маргарита')

        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')
        collector.set_book_genre('Война и мир', 'Комедии')
        collector.set_book_genre('Мастер и Маргарита', 'Фантастика')

        assert collector.get_books_with_specific_genre('Фантастика') == [
            'Гордость и предубеждение',
            'Мастер и Маргарита'
        ]

    def test_get_books_genre_return_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')

        assert collector.get_books_genre() == {
            'Гордость и предубеждение': 'Фантастика'
        }

    def test_get_books_for_children_return_books_without_age_rating(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Кошмар на улице Вязов')
        collector.add_new_book('Шерлок Холмс')

        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')
        collector.set_book_genre('Кошмар на улице Вязов', 'Ужасы')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')

        assert collector.get_books_for_children() == [
            'Гордость и предубеждение'
        ]

    def test_add_book_in_favorites_add_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.add_book_in_favorites('Гордость и предубеждение')

        assert 'Гордость и предубеждение' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_delete_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.add_book_in_favorites('Гордость и предубеждение')
        collector.delete_book_from_favorites('Гордость и предубеждение')

        assert 'Гордость и предубеждение' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_return_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Война и мир')

        collector.add_book_in_favorites('Гордость и предубеждение')
        collector.add_book_in_favorites('Война и мир')

        assert collector.get_list_of_favorites_books() == [
            'Гордость и предубеждение',
            'Война и мир'
        ]
