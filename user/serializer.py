from .models import Teacher,Student
from rest_framework import serializers
from admins.serializer import Topic_Serializer




class Teacher_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


        

class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' 