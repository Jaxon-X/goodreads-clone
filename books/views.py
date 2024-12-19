from django.views.generic import ListView, DetailView

from django.shortcuts import render
from django.views import View
from books.models import  Book

class BooksView(ListView):
    template_name = 'books/books_list.html'
    queryset = Book.objects.all()
    context_object_name = 'books'


# class BooksView(View):
#
#     def get(self, request):
#
#         books = Book.objects.all()
#         context = {'books': books}
#         return render(request, 'books/books_list.html', context)



class BookDetailView(DetailView):
    template_name = 'books/book_detail.html'
    pk_url_kwarg = 'book_id'
    model = Book


# class BookDetailView(View):
#
#     def get(self, request, book_id):
#         book = Book.objects.get(pk=book_id)
#         context = {'book': book}
#         return render(request, "books/book_detail.html", context)