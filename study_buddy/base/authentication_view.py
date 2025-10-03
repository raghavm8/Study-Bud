from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

    
def login_page(request):
    print("inside login")

    if request.user.is_authenticated:
        return redirect("Home")

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
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
    form = UserCreationForm()
    
    if request.user.is_authenticated:
        return redirect("Home")
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            print(user.username)
            user.save()
            login(request, user)
            return redirect("Home")
        else: 
            messages.error(request, "An error occured during registration")
            
            
    context = {"form": form}
    return render(request, "register.html", context)


def logout_page(request):
    logout(request)
    return redirect("LoginUser")
