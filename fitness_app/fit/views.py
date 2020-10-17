from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import *



def index(request):
    return render(request , 'fit/home.html', {'text':"Hello "})

def login_get(request):
    return render(request,'fit/login.html')

def signup_get(request):
    return render(request,'fit/signup.html')

