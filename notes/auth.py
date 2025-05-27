from django.shortcuts import render,redirect

def login(request):
    return render(request,"notes/login.html")