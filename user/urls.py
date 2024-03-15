from django.urls import path
from . import views


urlpatterns = [
    path('teacher/',views.Teacher_View.as_view(),name = "teacher_views")
   
     
]
