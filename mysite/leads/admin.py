from django.contrib import admin

# Register your models here.
from .models import Razze, Cani

admin.site.register(Razze)
admin.site.register(Cani)