from django.urls import path,re_path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView )
from . import views



urlpatterns=[
    path('',PostListView.as_view(), name='blog-home'),
    path('post/new/',PostCreateView.as_view(), name='post_create'),
    path('user/<str:username>/',UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post_detail'),
    # re_path('post/(?P<slug>[-\w]+)/',PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post_delete'),
    # path('about/',views.about,name='blog-about'),
    path('users/',views.searchposts,name='search')
    # path('users/',views.authors,name='author')
]

#(success_url = ('post_detail'))