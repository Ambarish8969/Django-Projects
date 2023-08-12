from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=100,null=True)
    email=models.EmailField(null=True)
    mobile=models.BigIntegerField(null=True)
    password=models.CharField(max_length=900,null=True)