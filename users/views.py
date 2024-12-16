from django.contrib import messages

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from users.forms import UserCreateForm, ProfileUpdateForm


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
            messages.success(request, "You have successfully logged in.")
            return redirect("books:list")
        else:
            context = {'form': AuthenticationForm()}
            return render(request, 'users/login.html', context )

class ProfileView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'users/profile.html')


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, "You have been logged out.")
        return redirect('landing_page')

class ProfileView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request, 'users/profile.html')


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.info(request, "You have been logged out.")
        return redirect('landing_page')

class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        user_update_form = ProfileUpdateForm(instance=request.user)
        context = {'form': user_update_form}
        return render(request, 'users/profile_edit.html', context)

    def post(self, request):
        user_update_form = ProfileUpdateForm(instance=request.user, data = request.POST)
        if user_update_form.is_valid():
            user_update_form.save()
            messages.success(request, "You have successfully updated.")
            return redirect('users:profile')
        else:
            context = {'form': user_update_form}
            return render(request, 'users/profile_edit.html', context)