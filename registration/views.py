from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView, CreateView
from .models import *
from .forms import *


def email(request):
    subject = 'Welcome to Celebs Resort'
    message = ''
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['nkpc14@gmail.com', ]
    send_mail(subject, message, email_from, recipient_list)
    return redirect('redirect to a new page')


class UserCreate(CreateView):
    template_name = 'BookNow.html'
    queryset = UserDetails.objects.all()
    success_url = '/'
    # form_class = UserForm
    fields = '__all__'

    def post(self, request, *args, **kwargs):
        subject = 'Welcome to Celebs Resort'
        message = ('Congratulations you have been registered successfully!\n Your Details are: '
                   + 'Name: ' + request.POST['name'] + '\n'
                   + 'Email: ' + request.POST['email'] + '\n'
                   + 'Phone: ' + request.POST['phone'] + '\n'
                   + 'No of Children: ' + request.POST['no_of_child'] + '\n'
                   + 'No of Adults: ' + request.POST['no_of_adult'] + '\n'
                   + 'Check In: ' + request.POST['check_in'] + '\n'
                   + 'Check Out: ' + request.POST['check_out'] + ''
                   )
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['celebsresortshimla@gmail.com', request.POST['email']]
        send_mail(subject, message, email_from, recipient_list)
        return super().post(request, *args, **kwargs)


class QueryCreate(CreateView):
    template_name = 'ContactUsResort.html'
    queryset = Query.objects.all()
    success_url = '/'
    # form_class = UserForm
    fields = '__all__'


class HomePageView(TemplateView):
    template_name = "AboutUsRestaurant.html"


class ContactUs(TemplateView):
    template_name = "ContactUsResort.html"


class BookNow(TemplateView):
    template_name = "BookNow.html"


class Adventure(TemplateView):
    template_name = "Adventure.html"


class BarsAndResorts(TemplateView):
    template_name = "BarsandResorts.html"


class Stories(TemplateView):
    template_name = "Stories.html"


class Private(TemplateView):
    template_name = "PrivateDining.html"
