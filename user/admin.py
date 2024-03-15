from django.contrib import admin
from .models import Teacher,Student
# Register your models here.



class Teacher_Admin(admin.ModelAdmin):
    list_display =[
        'user',
        'course',
        'topic',
        'subtopic'
        
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