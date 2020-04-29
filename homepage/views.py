from django.shortcuts import render

# Create your views her

def homepage(request):
    return render(request,"Home.html")