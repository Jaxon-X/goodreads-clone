from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
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
        return render(request, 'users/login.html')
