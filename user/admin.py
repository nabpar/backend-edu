from django.contrib import admin
from .models import Teacher,Student,TopicContent
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
    
    def formfield_for_foreignkey(self, db_field: ForeignKey[Any], request: HttpRequest | None, **kwargs: Any) -> ModelChoiceField | None:
             if db_field.name =='subject':
                   category_id = request.POST.get('category')
                   if category_id:
                         kwargs['queryset']= Subject.objects.filter(category_id=category_id)
                   else:
                         kwargs['queryset']= Subject.objects.none()      
             return super().formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(TopicContent,TopicContent_Admin)    