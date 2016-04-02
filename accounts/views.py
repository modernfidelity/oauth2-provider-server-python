from django.shortcuts import render
from django.http import HttpResponse


# Customer Login
def login(request):
    return render(request, 'accounts/login.html')


# Customer Login
def logout(request):
    return HttpResponse('hello')
