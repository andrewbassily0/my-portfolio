from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('resume', views.resume, name='resume'),
    path('portfolio', views.port, name='portfolio'),
    path('blog/<slug:slug>', views.post_detail, name='post_detail'),
]