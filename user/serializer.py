from .models import Teacher,Student,TopicContent
from rest_framework import serializers




class Teacher_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class TopicContent_Serializer(serializers.ModelSerializer):
    class Meta:
        model = TopicContent
        fields = '__all__'

class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'