from django.contrib import admin
from .models import Teacher,Student
from admins.models import Category,Subject
from django.db.models.fields.related import ForeignKey
from typing import Any
from django.http.request import HttpRequest
from django.forms.models import ModelChoiceField
# from admins.models import Topic
# Register your models here.



class Teacher_Admin(admin.ModelAdmin):
    list_display =[
        'user',
        'course',
        'topic'
        
    ]
admin.site.register(Teacher,Teacher_Admin)

class Student_Admin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'paid',
        'date'
    ]
admin.site.register(Student,Student_Admin)    


