from django.shortcuts import render, HttpResponse
from .models import User
from django.contrib.auth.hashers import (
    make_password,
)  # To encrypt the entered password in registration.
from django.contrib.auth.hashers import (
    check_password,
)  # To decrypt the entered password in login.
from django.contrib import messages  # To show messages in templates.
from django.contrib.auth import authenticate,login


# Create your views here.
def home(request):
    return HttpResponse("Ambarish Bhagawati")


def registration(request):
    if request.method == "POST":
        data = request.POST
        password = data.get("password")
        new_user = User.objects.create(
            username=data.get("username"),
            email=data.get("email"),
            mobile=data.get("mobile"),
            password=make_password(password),
        )
        new_user.save()
        messages.info(request, "Registration Completed.")
    return render(request, "form.html")


def loginPage(request):
    if request.method == "POST":
        data = request.POST
        # email = data.get("email")
        # password = data.get("password")
        if User.objects.filter(email=data.get("email")).exists():
            getuser = User.objects.get(email=data.get("email"))
            if check_password(data.get("password"), getuser.password):
                messages.success(request, "logged in successfully")
                
            else:
                messages.info(request, "Invalid password")
        else:
            messages.info(request, "Invlaid email Id")
        
        # user = authenticate(email=email, password=password)
        # print(user)
        # if user is None:
        #     messages.error(request,"invalid credentials 2222")
        # else:
        #     login(user)
        #     messages.success(request,"successfully logged in")

    return render(request, "login.html")
