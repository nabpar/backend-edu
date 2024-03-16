from django.contrib import admin
from .models import Teacher,Student,TopicContent
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


class TopicContent_Admin(admin.ModelAdmin):
    list_display = [
        'id',
        'teacher_name',
        'category',
        'subject',
        'topic',
        'content',
        'file_upload',
        'date_created',
        'date_updated'

        
    ]
admin.site.register(TopicContent,TopicContent_Admin)    