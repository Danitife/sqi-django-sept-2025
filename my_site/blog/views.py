from django.shortcuts import render, HttpResponse

# Create your views here.
def blog_page(request):
    return HttpResponse("Welcome to the Blog Home")

def blog_post1(request):
    return HttpResponse("This is Blog Post #1")

def about(request):
    return HttpResponse("About the Blog")