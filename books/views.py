from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from django.shortcuts import render, redirect
from django.template.base import kwarg_re
from django.urls import reverse
from django.views import View

from books.forms import BookReviewForm
from books.models import  Book, BookReview
class BooksView(View):

    def get(self, request):

        books = Book.objects.all().order_by('id')
        search_query = request.GET.get('q', "")
        if search_query:
            books = Book.objects.filter(title__icontains=search_query)
        page_size = request.GET.get('page_size' ,2)
        paginator = Paginator(books,page_size)

        page_num = request.GET.get('page',1)
        page_obj = paginator.get_page(page_num)

        return render(
            request,
            'books/books_list.html',
            {'page_obj': page_obj, "search_query":search_query}
        )


class BookDetailView(View):

    def get(self, request, book_id):
        book = Book.objects.get(pk=book_id)
        review_form = BookReviewForm()
        context = {'book': book, "form": review_form}
        return render(request, "books/book_detail.html", context)

class BookReviewView(LoginRequiredMixin, View):
    def post(self, request, book_id):
        book = Book.objects.get(pk=book_id)
        review_form = BookReviewForm(data=request.POST)

        if review_form.is_valid():
            BookReview.objects.create(
                book=book,
                user=request.user,
                comment = review_form.cleaned_data['comment'],
                stars_given = review_form.cleaned_data['stars_given'],
            )
            return redirect(reverse("books:detail", kwargs = {"book_id": book.id}))

        context = {'book': book, "form": review_form}
        return render(request, "books/book_detail.html", context)