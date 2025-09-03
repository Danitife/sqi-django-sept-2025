from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Welcome to the shop home")

def cart(request):
    return HttpResponse("Your shoppind cart is empty")
