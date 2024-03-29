from django.contrib import admin
from .models import *

# Register your models here.
class StudentAdminModel(admin.ModelAdmin):
    list_display=('id','name','age','city')
    list_filter = ('id', 'name')
    search_fields = ('id','name')

admin.site.register(Student,StudentAdminModel)

"""
    The choice between customizing the admin interface via admin.py and using serializers depends on the 
    requirements of your application. If you want to customize the admin interface specifically, 
    the admin.py approach provides more flexibility. If your focus is on API responses and you want to control 
    how data is presented in API views, then customizing serializers is more appropriate.
"""