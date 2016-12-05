from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from .forms import supportForm

# Create your views here.


def support(request):
    title = 'Customer Service & Support'
    form = supportForm(request.POST or None)
    context= {'title': title, 'form': form}

    if form.is_valid():
        print
        name = form.cleaned_data['Name']
        disputes = form.cleaned_data['Disputes']
        feedback = form.cleaned_data['Feedback']
        subject = 'Message from SHU Financial'
        message = '%s %s %s' %(name, disputes, feedback)
        emailfrom = form.cleaned_data['Email']
        emailto = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailfrom, emailto, fail_silently=True)
        title = "Thank You!"
        confirm_message = "We will get back to you as soon as possible!"
        context = {'title': title, 'confirm_message': confirm_message}
    template = 'support.html'
    return render(request, template, context)

