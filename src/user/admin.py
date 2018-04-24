from django.contrib import admin
from .models import (
    Frecuency, 
    Newsletter, 
    Profile
)
# Register your models here.

# admin.site.register(Frecuency)
admin.site.register(Newsletter)
admin.site.register(Profile)