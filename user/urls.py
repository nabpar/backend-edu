from django.urls import path
from . import views


urlpatterns = [
    path('teacher/',views.Teacher_View.as_view(),name = "teacher_views"),
    #  url  for the list view
    # path('topic_content_listapiview/',views.TopicContent_View.as_view(),name = "topiccontent_list"),
    # path('topic_content_edit/<int:pk>/',views.TopicContent_View.as_view(),name = "topiccontent_edit"),   
     
]
