from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Posts 
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home (request):
    return render(request, 'home.html')


def blog (request):
    posts = Posts.objects.all()
    return render(request, 'index.html', {'posts': posts})


def resume(request):
    profile = profile.objects.all()
    return render(request, 'Resume.html', {'profile':profile})

def port (request):
    return render(request, 'port.html')

def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(name,email,subject,message,[settings.EMAIL_HOST_USER],)
        return redirect('home')

    return render(request, 'contact.html')

def post_detail (request, slug):
    post = Posts.objects.get(slug=slug)
    context = {'post':post}
    return render(request, 'post_detail.html', context)


