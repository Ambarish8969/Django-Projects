from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=100)
    age=serializers.IntegerField()
    city=serializers.CharField(max_length=50)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

"""
    The choice between customizing the admin interface via admin.py and using serializers depends on the 
    requirements of your application. If you want to customize the admin interface specifically, 
    the admin.py approach provides more flexibility. If your focus is on API responses and you want to control 
    how data is presented in API views, then customizing serializers is more appropriate.
"""
