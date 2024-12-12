from django.contrib import admin
from django.urls import path

from goodreads.views import landing_page

urlpatterns = [
    path("", landing_page, name="landing_page"),
    path('admin/', admin.site.urls),
]


