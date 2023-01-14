from django import forms
from django.contrib import admin
from .models import Posts, Category , profile

admin.site.register(Posts)
admin.site.register(Category)
admin.site.register(profile)

