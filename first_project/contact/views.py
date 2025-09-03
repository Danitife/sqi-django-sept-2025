from django.shortcuts import render, HttpResponse

# Create your views here.

def phone_us(request):
    return HttpResponse ("Phone us: +2348177844692")

def email_us(request):
    return HttpResponse("Email us: daniel@gmail.com")