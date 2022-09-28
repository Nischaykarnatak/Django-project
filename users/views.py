from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from . forms import UserRegistration


# Create your views here.

def home(request):
    return render(request, 'users/index.html')


def profile(request):
    return render(request, 'users/profile.html')


def login(request):
    return render(request, 'users/login.html')


def logout(request):
    return render(request, 'logout.html')


def register(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('index')

    else:
        form = UserRegistration()
    return render(request, 'users/register.html', {'form': form})
