from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipie(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    recipie_name=models.CharField(max_length=200,null=True)
    recipie_description=models.TextField(max_length=1000,null=True)