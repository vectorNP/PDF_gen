from django.contrib import admin
from .models import Sales
from .models import Products


admin.site.register(Sales)
admin.site.register(Products)
