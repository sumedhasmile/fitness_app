from django.urls import path 
from django.conf.urls.static import static
from django.conf import settings
from . import views
app_name = "fit"

urlpatterns = [
    path("", views.index , name = "index"),
    path("login" , views.login_get,name="login"),
    path("signup",views.signup_get,name="signup"),
    path("logout",views.logout_get,name= "logout"),
    path("signup_post",views.Signup,name="signup_post"),
    path("login_post",views.Login,name="login_post")
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
