from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST('username')
        email = request.POST('email')
        password = request.POST('password')
        confirm_pass = request.POST('confirmPass')

        if password == confirm_pass:
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                messages.info(request, 'User already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                return redirect('dashboard')
        else:
            messages.info(request, 'Passwords mismatch')
            return redirect('signup')
    else:
        return render(request, 'signup.html')
            
def dashboard(request):
    return render(request, 'dashboard.html')

def login(request):
    return render(request, 'login.html')
