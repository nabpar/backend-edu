from django.shortcuts import render
from .serializer import Teacher_Serializer,Student_Serializer
from rest_framework.views import APIView 
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from rest_framework import generics
# Create your views here.

class Teacher_View(APIView):
    permission_classes = [IsAdminUser]

    def post(self,request,format = None):
        serializer = Teacher_Serializer(data= request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self,request,format = None):
        request = Teacher_Serializer.objects.all()
        serializer = Teacher_Serializer(request,many = True)
        return Response(serializer.data)
    

    def put(self,request,pk, format = None):
        request = self.get_object(pk)
        serializer = Teacher_Serializer(request,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#  views for the student 
    
class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = Student_Serializer

class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = Student_Serializer