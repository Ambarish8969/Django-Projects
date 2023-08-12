from django.db import models

# Create your models here.
class Student(models.Model):
    # id=models.AutoField()
    name=models.CharField(max_length=100, null=True)
    age=models.IntegerField(null=True)
    marks=models.IntegerField(default=1,null=True)