from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def addrecipie(request,username):

    user=User.objects.get(username=username)
    data=Recipie.objects.filter(user_id=user.id)

    if request.method == "POST":
        recipie_name = request.POST.get("recipie_name")
        recipie_description = request.POST.get("recipie_description")
        recipie = Recipie.objects.create(
            recipie_name=recipie_name, 
            recipie_description=recipie_description,
            user_id=user.id,
        )
        recipie.save()
        return redirect(f'/addrecipie/{username}')
    return render(request, "addrecipie.html",{'username':username})

def updaterecipie(request,id):
    recipie=Recipie.objects.get(id=id)
    if request.method=='POST':
        recipie_name = request.POST.get("recipie_name")
        recipie_description = request.POST.get("recipie_description")
        
        recipie.recipie_name=recipie_name
        recipie.recipie_description=recipie_description
        recipie.save()
        return redirect('/')
    return render(request,'updaterecipie.html',context={'recipie_name':recipie.recipie_name,'recipie':recipie})

@login_required(login_url="login/")
def showrecipies(request):
    recipies=Recipie.objects.all()
    return render(request,'showrecipies.html',context={'recipies':recipies})

def deleterecipie(request,id):
    recipie=Recipie.objects.get(id=id)
    recipie.delete()
    return redirect('/')

def createuser(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
    return render(request,'register.html')

def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,"Invalid Username")
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)
        print(user)

        if user is None:
            messages.error(request,"invalid credentials 2222")
            return redirect('/login/')
        else:
            login(request,user)
            messages.success(request,"successfully logged in")
            return redirect('/')
        
    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')