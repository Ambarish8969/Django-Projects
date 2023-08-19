from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login ,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="loginuser/")
def createtodo(request,username):
    
    user=User.objects.get(username=username)
    data=Todo.objects.filter(user_id=user.id)
    
    if request.method=="POST":
        todo_text=request.POST.get('todo_text')
        user = request.user
        text=Todo.objects.create(
            todo_text=todo_text,
            user_id=user.id,
        )
        text.save()
        return redirect(f'/createtodo/{username}')
    return render(request,'createtodo.html',{'todos':data})

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
    return render(request,'createuser.html')

def loginuser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/loginuser/')
        
        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,"Invalid User")
            return redirect("/loginuser/")
        else:
            login(request,user)
            messages.success(request,"successfully logged in")
            return redirect(f'/createtodo/{username}')
    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/loginuser/')

def createtodolist(request):
    return redirect('/loginuser/')