from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, MyPostsView, MySkillsView, SkillsCreateView
from django.views.generic import ListView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('mine/', MyPostsView.as_view(), name="my-posts"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('skill/new/', SkillsCreateView.as_view(), name="skills-create"),
    path('about/', views.about, name='blog-about'),
]