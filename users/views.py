from wsgiref.util import request_uri

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View
from users.forms import UserCreateForm


class RegisterView(View):
    def get(self, request):

        form = UserCreateForm()
        context = {'form': form}
        return render(request, 'users/register.html', context)

    def post(self, request):
        form = UserCreateForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
        else:
            context = {'form': form}
            return render(request, 'users/register.html', context)



class LoginView(View):
    def get(self, request):
        context = {'form': AuthenticationForm()}
        return render(request, 'users/login.html', context)

    def post(self, request):
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("landing_page")
        else:
            context = {'form': AuthenticationForm()}
            return render(request, 'users/login.html', context )

