from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# from .forms import ProfileUpdateForm, UserUpdateForm
# from dashboard import views

# Create your views here.
def index(request):
    return render(request, 'index.html')

def log_out(request):
    logout(request)
    return redirect('/')

# Role selection view
def select_role(request):
    return render(request, 'select_role.html')


def role_form(request):
    role = request.GET.get('role')

    if role not in ['student', 'teacher']:
        return HttpResponseBadRequest("Invalid role selected.")

    context = {'role': role}
    return render(request, 'login.html', context)

@login_required
def profile(request):
    return render(request, 'profile.html')
    

@login_required
def edit_profile(request):
    # if request.method == 'POST':
    #     u_form = UserUpdateForm(request.POST, instance=request.user)
    #     p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    #     if u_form.is_valid() and p_form.is_valid():
    #         u_form.save()
    #         p_form.save()
    #         messages.success(request, 'Your profile has been updated successfully!')
    #         return redirect('profile')
    # else:
    #     # u_form = UserUpdateForm(instance=request.user)
    #     # p_form = ProfileUpdateForm(instance=request.user.profile)

    # # context = {
    # #     'u_form': u_form,
    # #     'p_form': p_form
    # # }

    return render(request, 'edit_profile.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_pass = request.POST['confirmPass']

        if password == confirm_pass:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'User already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, 
                                                email=email, 
                                                password=password)
                send_mail(
                    subject='Welcome to Eduflecta',
                    message='''Thank you for trusting us Eduflectra. 
                    Your success is our priority. We hope you learn a lot 
                    our courses and that they will suit your needs.''',
                    from_email=None,
                    recipient_list=[email],
                    fail_silently=False
                )
                user.save()
                return redirect('dashboard')
        else:
            messages.info(request, 'Passwords mismatch')
            return redirect('signup')
    else:
        return render(request, 'signup.html')
            
# def dashboard(request):
#     return render(request, 'dashboard.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

def course(request):
    return render(request, 'course.html')


def about(request):

    return render(request, 'about.html')

def contact_view(request):  # Ensure this function name matches the one in urls.py
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            # Process the form data (e.g., send an email)
            return redirect('submission_successful')
        else:
            error_message = "Please fill out all fields correctly."
            return render(request, 'contact.html', {'error_message': error_message})
    else:
        return render(request, 'contact.html')

def submission_successful_view(request):
    return render(request, 'submission_successful.html')

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

