from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout

def login_page(request):
    print("inside login")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            print("User does not exist")
            messages.error(request, "User does not exist")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("Home")
        else:
            print(user)
            messages.error(request, "Username or password does not exist")
        
    context = {}
    return render(request, "login.html", context)

def register_page(request):
    context = {}
    return render(request, "login.html", context)

def logout_page(request):
    logout(request)
    return redirect("LoginUser")

