from django.urls import path 
from . import views
app_name = "fit"

urlpatterns = [
    path("", views.index , name = "index"),
    path("login" , views.login_get,name="login"),
    path("signup",views.signup_get,name="signup")
]
