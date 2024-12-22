from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

from django.shortcuts import render
from django.views import View
from books.models import  Book

class BooksView(ListView):
    template_name = 'books/books_list.html'
    queryset = Book.objects.all()
    context_object_name = 'books'
    paginate_by = 2

# class BooksView(View):
#
#     def get(self, request):
#
#         books = Book.objects.all().order_by('id')
#         page_size = request.GET.get('page_size' ,2)
#         paginator = Paginator(books,page_size)
#
#         page_num = request.GET.get('page',1)
#         print(page_num)
#         page_obj = paginator.get_page(page_num)
#         print(page_obj.object_list)
#         context = {'page_obj': page_obj}
#
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