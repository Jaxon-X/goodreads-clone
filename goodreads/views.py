from django.shortcuts import render

from books.models import BookReview


def landing_page(request):
    return render(request, "landing.html")

def home_page(request):
    book_review = BookReview.objects.all().order_by('-created_at')
    return render(request, "home.html", {'book_reviews': book_review})