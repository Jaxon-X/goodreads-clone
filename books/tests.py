
from django.test import TestCase
from django.urls import reverse
from books.models import Book


class BooksTestCase(TestCase):
    def test_no_books(self):
        response = self.client.get(reverse('books:list'))

        self.assertContains(response, 'No books found.')

    def test_books_list(self):
        book1 = Book.objects.create(title='Book 1', description='desc1', isbn='11223')
        book2 = Book.objects.create(title='Book 2', description='desc2', isbn='343242')
        book3 = Book.objects.create(title='Book 3', description='desc3', isbn='242455')

        response = self.client.get(reverse('books:list') + "?page_size=2")
        for book in [book1, book2]:
            self.assertContains(response, book.title)

        self.assertNotContains(response, book3.title)
        response2 = self.client.get(reverse('books:list') + "?page=2&page_size=2")
        self.assertContains(response2, book3.title)


    def test_book_detail(self):
        book = Book.objects.create(title='Book1', description='desc1', isbn='11223')
        response = self.client.get(reverse('books:detail', kwargs={'book_id': book.id}))
        self.assertContains(response, book.title)
        self.assertContains(response, book.description)

    def test_search_book(self):
        book1 = Book.objects.create(title='sport', description='desc1', isbn='11223')
        book2 = Book.objects.create(title='car', description='desc2', isbn='343242')
        book3 = Book.objects.create(title='Adabiyot', description='desc3', isbn='242455')

        response = self.client.get(reverse('books:list') + "?q=sport")
        self.assertContains(response, book1.title)
        self.assertNotContains(response, book2.title)
        self.assertNotContains(response, book3.title)
        response = self.client.get(reverse('books:list') + "?q=car")
        self.assertContains(response, book2.title)
        self.assertNotContains(response, book1.title)
        self.assertNotContains(response, book3.title)
        response = self.client.get(reverse('books:list') + "?q=Adabiyot")
        self.assertContains(response, book3.title)
        self.assertNotContains(response, book2.title)
        self.assertNotContains(response, book1.title)

