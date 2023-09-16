from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['POST'])
def createuser(request):
    if request.method == 'POST':
        serializer=UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        
        
@api_view(['POST'])
def createtodo(request,username):
    user=User.objects.get(username=username)
    if request.method=='POST':
        serializer=TodoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])
def getalltodos(request):
    todos=Todo.objects.all()
    serializer=TodoSerializer(todos,many=True)
    return Response(serializer.data,status=status.HTTP_302_FOUND)

@api_view(['GET'])
def gettodobyusername(request,username):
    user=User.objects.get(username=username)
    todos=Todo.objects.filter(user_id=user.id)
    serializer=TodoSerializer(todos,many=True)
    return Response(serializer.data,status=status.HTTP_302_FOUND)

@api_view(['DELETE'])
def deletetodobyid(request,username,tid):
    user = get_object_or_404(User, username=username)
    todo = get_object_or_404(Todo, user=user, id=tid)

    todo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)