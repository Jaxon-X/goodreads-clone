
from django.urls import path, include

from books.views import BooksView, BookDetailView

app_name = 'books'
urlpatterns = [
    path("", BooksView.as_view(), name="list"),
    path("<int:book_id>/", BookDetailView.as_view(), name="detail"),
]