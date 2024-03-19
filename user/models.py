# from django.db import models
# from Accounts.models import User
# from admins.file_upload import Uploader

# # Create your models here.


# # class Teacher(models.Model):
# #     user = models.ForeignKey(User,on_delete = models.CASCADE)
# #     message = models.TextField()
# #     is_approved = models.BooleanField(default = False)
# #     date_created = models.DateTimeField(auto_now_add = True)


# #     def __str__(self):
# #         return f"Teacher Request - {self.user.email}"


# class Teacher(models.Model):
#     user = models.ForeignKey(User, on_delete = models.CASCADE)
#     course = models.ForeignKey(Category,on_delete = models.CASCADE,blank = True)
#     subject = models.ForeignKey(Subject, on_delete = models.CASCADE,blank = True)
#     topic = models.ForeignKey(Topic, on_delete = models.CASCADE,blank = True)
#     subtopic = models.ForeignKey(Subtopic,on_delete = models.CASCADE,blank = True)

#     def __str__(self):
#         return self.user.name




#     def get_subject_by_id(category_id):
#         if category_id:
#             return Subject.objects.filter(category = category_id)
        
#         else:
#             return Subject.objects.none()
        
#     def get_topic_by_id(subject_id):
#         if subject_id:
#             return Topic.objects.filter(subject = subject_id)

#         else:
#             return Topic.objects.none()


#     def get_subtopic_by_id(topic_id):
#         if topic_id:
#             return Subtopic.objects.filter(topic = topic_id)
#         else:
#             return Subtopic.objects.none()        





# class Student(models.Model):
#     user = models.ForeignKey(User, on_delete = models.CASCADE)
#     enroll_course = models.ManyToManyField(Category,related_name= "enroll_course")
#     paid = models.BooleanField(default = False)
#     date = models.DateTimeField( auto_now_add = True)


#     def __str__(self) -> str:
#         return self.user.name


from django.db import models
from Accounts.models import User
# from admins.models import Subject,Topic,Subtopic
from admins.file_upload import Uploader
from admins.base_class import BaseClass 

# Create your models here.

def TopicFiles(instance,filename):
    return "topic_content_files/{filename}".format(filename=filename)


# class Teacher(models.Model):
#     user = models.ForeignKey(User,on_delete = models.CASCADE)
#     message = models.TextField()
#     is_approved = models.BooleanField(default = False)
#     date_created = models.DateTimeField(auto_now_add = True)


#     def __str__(self):
#         return f"Teacher Request - {self.user.email}"


class Teacher(models.Model):
    user = models.ForeignKey('Accounts.User', on_delete = models.CASCADE)
    course = models.ForeignKey('admins.Category',on_delete = models.CASCADE,blank = True)
    subject = models.ForeignKey('admins.Subject', on_delete = models.CASCADE,blank = True)
    topic = models.ForeignKey('admins.Topic', on_delete = models.CASCADE,blank = True)
    # subtopic = models.ForeignKey(Subtopic,on_delete = models.CASCADE,blank = True)

    def __str__(self):
        return self.user.name




    def get_subject_by_id(category_id):
        from admins.models import Subject
        if category_id:
            return Subject.objects.filter(category = category_id)
        
        else:
            return Subject.objects.none()
        
    def get_topic_by_id(subject_id):
        from admins.models import Topic
        if subject_id:
            return Topic.objects.filter(subject = subject_id)

        else:
            return Topic.objects.none()
    # def get_    


    # def get_subtopic_by_id(topic_id):
    #     if topic_id:
    #         return Subtopic.objects.filter(topic = topic_id)
    #     else:
    #         return Subtopic.objects.none()        


class TopicContent(models.Model):
    # teacher = models.ForeignKey(User, on_delete  = models.CASCADE, related_name = "teacher_name")
    teacher_name = models.ForeignKey(User, on_delete = models.CASCADE,blank = True,null = True)
    category = models.ForeignKey('admins.Category', on_delete= models.CASCADE)
    subject = models.ForeignKey('admins.Subject', on_delete= models.CASCADE)
    topic = models.TextField()
    content =  models.TextField()
    file_upload = models.FileField(upload_to=TopicFiles,blank=True,null = True)
    date_created = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    date_updated = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    # added_by = models.ForeignKey('Accounts.User', on_delete = models.CASCADE,blank = True,null = True)
    # updated_by
    # status = enum  verify unverified default un verified.
    # publish = 
    # un_publish
    # publis

    
    def __str__(self):
        return f"{self.category}-{self.subject}"
    

    def get_subject_by_id(category_id):
        from admins.models import Subject
        if category_id:
            return Subject.objects.filter(category = category_id)
        else:
            return Subject.objects.filter.none()

    def __str__(self):
        return self.teacher_name.name
    # def __str__(self):
    #     if self.teacher_name:
    #         return f" content added by, {self.teacher_name.name}"
    #     else:
    #         return "Content added without specifying teacher" 




class Student(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    enroll_course = models.ManyToManyField('admins.Category',related_name= "enroll_course")
    paid = models.BooleanField(default = False)
    date = models.DateTimeField( auto_now_add = True)


    def __str__(self) -> str:
        return self.user.name
