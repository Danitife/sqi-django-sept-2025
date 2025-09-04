from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "single_app/home.html")
def help(request):
    return render(request, "single_app/help.html")
def profile(request):
    return render(request, "single_app/profile.html")
def services(request):
    return render(request, "single_app/services.html")