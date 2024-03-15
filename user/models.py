from django.db import models
from Accounts.models import User
from admins.models import Category,Subject,Topic,Subtopic
from admins.file_upload import Uploader

# Create your models here.


# class Teacher(models.Model):
#     user = models.ForeignKey(User,on_delete = models.CASCADE)
#     message = models.TextField()
#     is_approved = models.BooleanField(default = False)
#     date_created = models.DateTimeField(auto_now_add = True)


#     def __str__(self):
#         return f"Teacher Request - {self.user.email}"


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    course = models.ForeignKey(Category,on_delete = models.CASCADE,blank = True)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE,blank = True)
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE,blank = True)
    subtopic = models.ForeignKey(Subtopic,on_delete = models.CASCADE,blank = True)

    def __str__(self):
        return self.user.name




    def get_subject_by_id(category_id):
        if category_id:
            return Subject.objects.filter(category = category_id)
        
        else:
            return Subject.objects.none()
        
    def get_topic_by_id(subject_id):
        if subject_id:
            return Topic.objects.filter(subject = subject_id)

        else:
            return Topic.objects.none()


    def get_subtopic_by_id(topic_id):
        if topic_id:
            return Subtopic.objects.filter(topic = topic_id)
        else:
            return Subtopic.objects.none()        





class Student(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    enroll_course = models.ManyToManyField(Category,related_name= "enroll_course")
    paid = models.BooleanField(default = False)
    date = models.DateTimeField( auto_now_add = True)


    def __str__(self) -> str:
        return self.user.name
