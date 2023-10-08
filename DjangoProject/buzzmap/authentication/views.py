from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Import your models here
from .models import User, Bus, Route

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('Password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your home page URL
        else:
            messages.error(request, 'Invalid credentials. Please try again.')

    return render(request, 'login.html')

@login_required
def home(request):
    # Add logic for the home page view here
    return render(request, 'home.html')
