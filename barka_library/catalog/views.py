from django.shortcuts import render, HttpResponse

# Create your views here.
def books(request):
    return HttpResponse("""
        <ul>
            <ol>Stone is hard</ol>
            <ol>Python is deadly</ol>
            <ol>Water is liquid</ol>
            <ol>Water is liquid</ol>
        </ul>
    """)
