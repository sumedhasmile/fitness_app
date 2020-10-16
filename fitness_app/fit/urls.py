from django.urls import path 
from . import views
app_name = "fit"

urlpatterns = [
    path("", views.index , name = "index")
]
