from django.shortcuts import render
from django.views import View

class RegisterView(View):
    def get(self, request):
        return render(request, 'users/register.html')



class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')
