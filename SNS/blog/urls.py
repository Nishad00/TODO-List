from django.urls import path
from .views import PostListView,  PostCreateView, PostUpdateView, PostDeleteView
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home' ),

    path("post/new/", PostCreateView.as_view(), name="post-create"),
   
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),

    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),

]


