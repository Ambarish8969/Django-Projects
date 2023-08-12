from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    if request.method=='POST':
        data=request.POST
        Student.objects.create(
            name=data.get('name'),
            age=data.get('age'),
            marks=data.get('marks'),
        )
    return render(request,"index.html")

def getall(request):
    if request.method=='GET':
        list1=(Student.objects.all())
    return render(request,'allstudents.html',context={'students':list1})

def deleteStudent(request,id):
    queryset=Student.objects.get(id=id)
    queryset.delete()
    return redirect('/')

def updateStudent(request,id):
    queryset=Student.objects.get(id=id)
    if request.method=='POST':
        data=request.POST
        queryset.name=data.get('name')
        queryset.age=data.get('age')
        queryset.marks=data.get('marks')
        queryset.save()
        return redirect('/')
    return render(request,'updatestudent.html',context={'student':queryset})