from django.urls import path
from . import views


urlpatterns = [
    path('teacher/',views.Teacher_View.as_view(),name = "teacher_views"),
    #  url  for the list view
    # path('topic_content_listapiview/',views.TopicContent_View.as_view(),name = "topiccontent_list"),
    # path('topic_content_edit/<int:pk>/',views.TopicContent_View.as_view(),name = "topiccontent_edit"),


    # #  generics Api
    path('topic_content_listview/',views.TopicContent_ListView.as_view(),name="view_Topic_content"),
    path('topic_content_create/',views.TopicContent_CreateView.as_view(),name="create_Topic_content"),
    path('topic_content_update/<int:pk>/',views.TopicContent_UpdateView.as_view(),name="updateTopic_content"),
    path('topic_content_delete/<int:pk>/',views.TopicContent_DestroyView.as_view(),name="delete topic content")
   
     
]
