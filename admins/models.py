from django.db import models
from .base_class import BaseClass
from django.utils.text import slugify
from user.models import Teacher,TopicContent


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

class Topic(models.Model):

    class Select(models.TextChoices):
        unverify = 'unverify'
        verify = 'verify'

    category = models.ForeignKey(Category, on_delete= models.CASCADE,default=1)
    subject = models.ForeignKey(Subject, on_delete= models.CASCADE,default=1)
    # topics = models.OneToOneField(TopicContent,on_delete = models.CASCADE,related_name = "topics_from_teacher",null = True,blank = True)
    topic_content = models.OneToOneField(TopicContent, on_delete = models.CASCADE,related_name = "content_from_teacher",blank = True,null = True)
    name = models.CharField(max_length = 255 , blank = True,null= True)
    # content =  models.TextField(blank = True,null = True)
    added_by = models.OneToOneField(TopicContent,on_delete = models.CASCADE,related_name = "updated_by_teacher",blank = True,null = True)
    updated_by = models.CharField(max_length = 255,blank = True,null = True)
    # status = enum  verify unverified default un verified.
    status = models.CharField(choices =Select.choices,max_length = 255,null = True,blank = True,default = Select.unverify)
    date_created = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    date_updated = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    # publish = 
    # un_publish
    # publis



    # def __str__(self):
    #     return self.name
    def __str__(self):
        return self.added_by.teacher_name

    class Meta(BaseClass.Meta):
        db_table = "admins_topic"


# class Subtopic(BaseClass):
#     category=models.ForeignKey(Category,on_delete=models.CASCADE)
#     subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
#     topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
#     slug=models.SlugField(blank= True, null= True)

#     def __str__(self):
#         return self.name
 
    
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
