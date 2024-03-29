"""
URL configuration for emailsender project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from emailapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',send_email,name="send_email"),
    path('captchacode/<int:length>',captchaGenerator,name='captchaGenerator'),
    path('dictonaryweb/<str:word>',dictonaryweb,name='dictonaryweb'),
    path('dictionaryapi/<str:word>',dictionaryapi),

  # REST APIs of Student 
    path('studentinfo/<int:id>',getstudent,name="getstudent"),
    path('studentinfo/',studentall,name="studentall"),
    path('createstudent/',createstudent,name="createstudent"),
    path('updatestudent/<int:id>',updatestudent,name="updatestudent"),
    path('deletestudent/<int:id>',deletestudent,name="deletestudent"),
]
