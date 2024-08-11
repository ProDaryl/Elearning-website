from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    return HttpResponse('<h1>Welcome</h1>')

def register(request):
    pass

def login(request):
    pass
