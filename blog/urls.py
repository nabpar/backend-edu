from django.urls import path

from blog import views


urlpatterns = [
    # this is the Blog Url
    path("view_blogs/", views.View_Blog.as_view(), name="ViewBlogs"),
    path("view_blogs/<int:pk>/", views.Retrieve_Blog.as_view(), name="GetBlog"),
    path("create_blogs/", views.Create_Blog.as_view(), name="CreateBlogs"),
    path("update_blogs/", views.Upadate_Blog.as_view(), name="Upadate_Blogs"),
    path("delete_blogs/<int:pk>/", views.Destroy_Blog.as_view(), name="Destroy_Blogs"),


# Urls of  the Comments 
    path("comments", views.Create_Comment.as_view()),
    path("comments/<int:pk>/", views.Single_Comment.as_view()),


    path("search_blogs/",views.SearchList.as_view(),name="SearchBlogs"),
    # path('mmvs/',views.MyModelViewSet.as_view(),name="viewset"),
]
