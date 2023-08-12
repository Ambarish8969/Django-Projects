from django.shortcuts import render,HttpResponse
from .models import User
from django.contrib.auth.hashers import make_password    # To encrypt the entered password in registration.
from django.contrib.auth.hashers import check_password   # To decrypt the entered password in login.
from django.contrib import messages                      # To show messages in templates. 
from django.core.exceptions import ValidationError


# Create your views here.
def home(request):
    return HttpResponse("Ambarish Bhagawati")

def registration(request):
    if request.method=='POST':
        data=request.POST
        password=data.get('password')
        new_user = User.objects.create(
            username=data.get('username'),
            email=data.get('email'),
            mobile=data.get('mobile'),
            password=make_password(password)
        )
        new_user.save()

    return render(request,'form.html')

def login(request):
    if request.method=='POST':
        data=request.POST
        getuser=User.objects.get(email=data.get('email'))
        if(check_password(data.get('password'),getuser.password)):
            print("logged in successfully")
            messages.success(request,"logged in successfully")
        else:
            print("invalid credentials")
            messages.info(request,"invalid credentials")

    return render(request,'login.html')