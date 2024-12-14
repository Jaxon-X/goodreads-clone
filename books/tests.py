
from django.test import TestCase
from django.urls import reverse
from books.models import Book


class BooksTestCase(TestCase):
    def test_no_books(self):
        repsonse = self.client.get(reverse('books:list'))

        self.assertContains(repsonse, 'No books found.')

    def test_books_list(self):
        book1 = Book.objects.create(title='Book 1', description='desc1', isbn='11223')
        book2 = Book.objects.create(title='Book 2', description='desc2', isbn='343242')
        book3 = Book.objects.create(title='Book 3', description='desc3', isbn='242455')

        response = self.client.get(reverse('books:list'))
        books = Book.objects.all()
        for book in books:
            self.assertContains(response, book.title)

        books_count = Book.objects.count()
        self.assertEqual(books_count, 3)

    def test_book_detail(self):
        book = Book.objects.create(title='Book1', description='desc1', isbn='11223')
        response = self.client.get(reverse('books:detail', kwargs={'book_id': book.id}))
        self.assertContains(response, book.title)
        self.assertContains(response, book.description)
        print(response)