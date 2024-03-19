from .models import Teacher,Student,TopicContent
from rest_framework import serializers




class Teacher_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class TopicContent_Serializer(serializers.ModelSerializer):
    # teacher_name= serializers.SerializerMethodField()

    class Meta:
        model = TopicContent
        # fields = ["teacher_name","category","subject","topic","content","file_upload","date_created","data_updated"]
        fields = '__all__'
        

    




class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' 