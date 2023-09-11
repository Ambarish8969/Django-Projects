from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,"Invalid Username")
            return redirect('/userlogin/')
        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'Invalid credentials')
            return redirect('/userlogin/')
        else:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('/showallrecipes/')
    return render(request,'login.html')

def user_registration(request):
    if request.method == 'POST':
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        user.set_password(password)
        user.save()
        return redirect('/userlogin/')
    return render(request,'registration.html')

# @login_required
def addrecipe(request):
    if request.method == 'POST':
        recipe_name = request.POST['recipe_name']
        recipe_description = request.POST['recipe_description']
        # Create a new Recipe instance and save it to the database
        recipe = Recipe(
            recipie_name=recipe_name, 
            recipie_description=recipe_description, 
            user=request.user
        )
        recipe.save()
        # Redirect to a success page or recipe list page
        return redirect('/showallrecipes/')
    return render(request,'addrecipe.html')

def updaterecipe(request,id):
    recipe=Recipe.objects.get(id=id)
    if request.method == 'POST':
        recipe_name=request.POST.get('recipe_name')
        recipe_description=request.POST.get('recipe_description')

        recipe.recipie_name=recipe_name
        recipe.recipie_description=recipe_description
        recipe.save()
        return redirect('/showallrecipes/')
    return render(request,'updaterecipe.html',context={'recipe_name':recipe.recipie_name,'recipe':recipe})

def deleterecipie(request,id):
    recipie=Recipe.objects.get(id=id)
    recipie.delete()
    return redirect('/showallrecipes/')

def showrecipes(request):
    user_recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'showrecipes.html', {'user_recipes': user_recipes,'user':request.user})

def user_logout(request):
    logout(request)
    return redirect('/userlogin/')

def welcomeview(request):
    return render(request,'welcome.html')