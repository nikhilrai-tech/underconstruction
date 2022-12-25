from django.shortcuts import render

def home(request):
    print("i am home view")
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")
