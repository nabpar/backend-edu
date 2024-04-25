from typing import Iterable
from django.db import models
from .base_class import BaseClass
from django.utils.text import slugify
from Accounts.models import User

# Create your models here.
class Category(BaseClass):
    # id = models.IntegerField(primary_key=True)
    slug = models.SlugField(blank=True,null=True)
    class Meta(BaseClass.Meta):
        db_table = "admins_category"


    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        self.slug = slugify(self.slug)
        super(Category,self).save(*args,**kwargs)

    def get_related_subjects(self):
        return self.subjects.all()     
       
            

    def __str__(self):
        return self.name    
  

class Subject(BaseClass):
    code = models.IntegerField(unique=True)   
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1) 
    class Meta(BaseClass.Meta):
        db_table = "admins_subject"

    def __str__(self):
        return self.name   

class Topic(BaseClass):

    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete= models.CASCADE)
    name = models.CharField(max_length = 255 )
    assign_to = models.ForeignKey(User, on_delete = models.CASCADE,related_name='assigned_topics')

    def __str__(self):
        return f"{self.category.name}-{self.subject.name}-{self.name}"
    

    def get_subject_by_id(category_id):
        if category_id:
            return Subject.objects.filter(category = category_id)
        else:
            return Subject.objects.filter.none()
    
    class Meta(BaseClass.Meta):
        db_table = "admins_topic"


def TopicFiles(instance,filename):
    return "topic_content_files/{filename}".format(filename=filename)

class TopicContent(models.Model):
    class Status(models.TextChoices):
        DRAFT='DRAFT','DRAFT'
        REVIEW='REVIEW','REVIEW'
        REJECTED='REJECTED','REJECTED'
        PUBLISHED='PUBLISHED','PUBLISHED'

    topic = models.OneToOneField(Topic,on_delete=models.CASCADE,related_name='content')
    content =  models.TextField()
    file_upload = models.FileField(upload_to=TopicFiles,blank=True,null = True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=15,choices=Status.choices,default=Status.DRAFT)
    status_message=models.CharField(max_length=255,null=True,blank=True)

    
    def __str__(self):
        return f"{self.category}-{self.subject}"
    

    def __str__(self):
        return self.teacher_name.name

 
    
class Syllabus(BaseClass):
   
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,null=True)
    syllabus_file=models.FileField(upload_to='syllabus/files',blank=True,null=True)
    

    def __srt__(self):
        return self.name



class ContactLeads(BaseClass):

    class ContactStatus(models.TextChoices):
        RESOLVED='RESOLVED'
        PENDING='PENDING'
        IN_PROGRESS='IN_PROGRESS'
        SPAM='SPAM'

    name=models.CharField(max_length=120)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    message=models.TextField()
    status=models.CharField(max_length=20,choices=ContactStatus.choices,default=ContactStatus.PENDING)
