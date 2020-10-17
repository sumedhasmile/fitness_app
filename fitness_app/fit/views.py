from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import *


# Create your views here.
<<<<<<< HEAD
def index(request):
    return render(request , 'fit/home.html', {'text':"Hello "})

def login_get(request):
    return render(request,'fit/login.html')

def signup_get(request):
    return render(request,'fit/signup.html')
=======
def Home(request):
    return render(request, 'home.html')


def Signup(request):
    if request.method == "POST":
        dic = request.POST
        u = dic['user']
        p = dic['pwd']
        mob = dic['mob']
        f = dic['fname']
        l = dic['lname']
        email = dic['email']
        age = dic['age']
        gender = dic['gender']
        weight = dic['weight']
        height = dic['height']
        img = request.FILES['img']
        userdata = User.objects.filter(username=u)
        if userdata:
            messages.error(request, 'User Already Exists')
            return redirect('Login')
        else:
            user = User.objects.create_user(first_name=f, last_name=l, username=u, password=p, email=email)
            User_details.objects.create(user=user, mobile_no=mob, profile_image=img, age=age, gender=gender,
                                        weight=weight, heigth=height)
            return redirect('Login')
    return render(request, 'fit/signup.html')


def Login(request):
    if request.method == "POST":
        dic = request.POST
        u = dic['user']
        p = dic['pwd']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User not found')
            return redirect('Login')

    return render(request, 'fit/login.html')


def Add_Task(request):
    if request.method == "POST":
        dic = request.POST
        title = dic['title']
        task_date = dic['task_date']
        due_date = dic['due_date']
        Goals.objects.create(task_name=title, Task_date=task_date, Due_date=due_date, user=request.user)
    return render(request, 'fit/add_task.html')
>>>>>>> 8c7e9091de1b9d1d41abf7cd2724c815d2a1dde9
