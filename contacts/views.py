from django.shortcuts import render 
from django.contrib import messages
from django.core.mail import send_mail



# Create your views here.
def cont(request):  
   if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        form_data = {
            'name':name,
            'email':email,
            'message':message,
        }
        message = '''
        From:\n\t\t{}\n
        Message:\n\t\t{}\n
        Email:\n\t\t{}\n
        '''.format(form_data['name'], form_data['message'], form_data['email'])
        send_mail('You got a mail ', message, email, ['vitobassily@gmail.com']) 
        messages.success(request, 'Your message has been sent successfully')
        return render(request, 'cont.html')
 
   return render(request, 'cont.html')
