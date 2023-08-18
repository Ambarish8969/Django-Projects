import io
from django.shortcuts import render 
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse,JsonResponse
import random, requests
from PyDictionary import PyDictionary
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer,status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def send_email(request):
    to_emails=[]
    if request.method=='POST':
        to_emails.append(request.POST.get('to-email'))
        subjectEmail=request.POST.get('subject-email')
        messageEmail=request.POST.get('message-email')
        print(to_emails)
        if subjectEmail and messageEmail:
            try:
                send_mail(subjectEmail,messageEmail,'ambarish.bhagawati8653@gmail.com',to_emails)
            except BadHeaderError:
                return HttpResponse("Invalid Header Found.")
        else:
            return HttpResponse("Mail send aagvato ambya.")
    return render(request,'sendmail.html')

def captchaGenerator(request,length):
    chars='abcdefghijklmnopqrstuvwxysABCDEFGHIJKLMNOPQRSTUVWXYS123456789'
    captchacode=''
    for i in range(length):
        captchacode=captchacode+random.choice(chars)
    return HttpResponse(captchacode)

# Dictonary API : https://api.dictionaryapi.dev/api/v2/entries/en/<word>

def dictonaryweb(request,word):
    data=PyDictionary()
    meanings=data.meaning(word)
    synonyms=data.synonym(word)
    antonyms=data.antonym(word)
    context={
        'meaning':meanings,
        'synonyms':synonyms,
        'antonyms':antonyms,
    }
    return render(request,'dictonaryweb.html',context=context)

def dictionaryapi(request,word):
    response=requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}").json()
    meanings=[]
    print(response[0]['meanings'][0]['definitions'])
    for i in range(len(response[0]['meanings'][0]['definitions'])):
        meanings.append(response[0]['meanings'][0]['definitions'][i]['definition'])

    # antonyms=response[0]['meanings'][2]['antonyms']
    context={
        'meanings':meanings,
        # 'antonyms':antonyms,
    }
    
    # first_entry = response[0]  # Get the first entry in the response
    # first_meaning = first_entry['meanings'][0]  # Get the first meaning in the first entry
    # definitions = [definition['definition'] for definition in first_meaning['definitions']]  # Extract 'definition' values

# # 'definitions' now contains a list of 'definition' values
#     print(definitions)
    print('---------------------------------------------------------------------------------------------------')
    print(meanings)
    # return HttpResponse('ambi')
    # return render(request,'dictonaryweb.html',context={'meanings':definitions})
    return render(request,'dictonaryweb.html',context=context)

# Method 1
def studeninfo(request,pk):
    stu=Student.objects.get(id=pk)
    serializer=StudentSerializer(stu)
    return JsonResponse(serializer.data,safe=False)

# Method 2
@api_view(['GET'])
def studentall(request):
    stu=Student.objects.all()
    serializer=StudentSerializer(stu,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST', 'GET'])
def hello_world(request):
    if request.method == 'GET':
        return Response({'message': 'This is a GET Request'})
    elif request.method == 'POST':
        return Response({'message': 'This is a POST Request'})