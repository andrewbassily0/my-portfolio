from django.urls import path 
from . import views

urlpatterns = [
    path('cont', views.cont, name='cont'),
   
]