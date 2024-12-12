from http.client import HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render


def landing_page(request):
    return render(request, "landing.html")