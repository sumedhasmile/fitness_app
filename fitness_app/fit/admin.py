from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User_details)
admin.site.register(Goals)
admin.site.register(Food_details)