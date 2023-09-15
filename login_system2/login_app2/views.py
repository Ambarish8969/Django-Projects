from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import *

# Create your views here.
def create_user(request):
    if request.method == 'POST':
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        username=request.POST['username']
        password=request.POST['password']
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        return redirect('/login/')
    return render(request,'registration.html')

def login_user(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            print("Invalid Username")
            return redirect('/login/')
        
        user=authenticate(username=username,password=password)

        if user is None:
            print("Invalid password")
            return redirect('/login/')
        else:
            print("loggedin successfully")
            login(request,user)
            return render(request,'welcome.html',{'user':user})
        
    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

# Using 'Django Forms' ------------------------------------->

def loginform(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user=authenticate(username=username,password=password)

            if user is None:
                print("Invalid password")
                return redirect('/loginform/')
            else:
                print("loggedin successfully")
                login(request,user)
                return render(request,'welcome.html',{'user':user})
    else:
        form=LoginForm()

    return render(request,'loginform.html',{'form': form})

def signupform(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user= User.objects.create(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                username=form.cleaned_data['username'],
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/signupform/')
    else:
        form=SignUpForm()
    return render(request,'signupform.html',{'form': form})

def logout_page2(request):
    logout(request)
    return redirect('/loginform/')