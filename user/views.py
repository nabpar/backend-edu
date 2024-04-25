from django.shortcuts import render
from .serializer import Teacher_Serializer,Student_Serializer
from admins.serializer import TopicContent_Serializer
from rest_framework.views import APIView 
from rest_framework.permissions import IsAdminUser,AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from admins.models import TopicContent
from rest_framework import generics
from rest_framework.generics import get_object_or_404,Http404
# Create your views here.

class Teacher_View(APIView):
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        req = TopicContent.objects.all()
        return req

    def post(self,request,format = None):
        serializer = Teacher_Serializer(data= request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self,request,format = None):
        id  = request.query_params["id"]
        if id != None:
            request = TopicContent.objects.get(id)
            serializer = TopicContent_Serializer(request)

        else:
            request = self.get_queryset()
            serializer = TopicContent_Serializer(request,many = True)
            return request


        # request = Teacher_Serializer.objects.all()
        # serializer = Teacher_Serializer(request,many = True)
        # return Response(serializer.data)
    

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


#  .....................api view for the TopicContent.....................................
    


# class TopicContent_View(APIView):
#     permission_classes = [AllowAny]   


#     def get_object(self,pk):
#         try:
#             return TopicContent.objects.get(id=pk)
#         except TopicContent.DoesNotExist:
#                 raise Http404
    
#     def post(self,request,format = None):
#         serializer = TopicContent_Serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    
#     def get(self ,request,format = None):

#         request = TopicContent.objects.all()
#         serializer = TopicContent_Serializer(request,many = True)
   
#         return Response(serializer.data)
    

    # def get(self,request,format = None):
    #     id  = request.query_params["id"]
    #     if id != None:
    #         request = TopicContent.objects.get(id)
    #         serializer = TopicContent_Serializer(request)

    #     else:
    #         request = self.get_queryset()
    #         serializer = TopicContent_Serializer(request,many = True)
    #         return request
        
#     def put(self,request,id,format = None):
#         request =  self.get_object(id)
#         serializer = TopicContent_Serializer(request,data=request.data)
#         if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
       
       
#     def delete(self,request,id,format = None):
#         request = self.get_object(id)
#         request.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    

