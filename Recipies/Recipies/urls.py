"""
URL configuration for Recipies project.

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
from recipie.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',showrecipies,name="showrecipies"),
    path('addrecipie/',addrecipie,name="addrecipie"),
    path('addrecipie/<str:username>',addrecipie,name="addrecipie"),
    path('updaterecipie/<id>',updaterecipie,name="updaterecipie"),
    path('deleterecipie/<id>',deleterecipie,name="deleterecipie"),
    path('register/',createuser,name="createuser"),
    path('login/',login_page,name="login_page"),
    path('logout/',logout_page,name="logout_page"),
]
