from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request , 'fit/home.html', {'text':"Hello "})

def login_get(request):
    return render(request,'fit/login.html')