from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

# Role selection view
def select_role(request):
    return render(request, 'select_role.html')

# Dynamic form view
def role_form(request):
    role = request.GET.get('role')

    if role not in ['student', 'teacher']:
        return HttpResponseBadRequest("Invalid role selected.")

    context = {'role': role}
    return render(request, 'login.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_pass = request.POST['confirmPass']

        if password == confirm_pass:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'User already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('dashboard')
        else:
            messages.info(request, 'Passwords mismatch')
            return redirect('signup')
    else:
        return render(request, 'signup.html')
            
def dashboard(request):
    return render(request, 'dashboard.html')

def course(request):
    return render(request, 'course.html')
# Teacher page view
def teacher(request):
    return render(request, 'teacher.html')

# About page view
def about(request):
    return render(request, 'about.html')

# Contact page view
def contact(request):
    return render(request, 'contact.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
     return render(request, 'login.html')
 
