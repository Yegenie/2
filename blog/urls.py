from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name="detail"),
    path('post/', views.post, name='post'),
    path('create/', views.create, name='create'),
    path('newblog/', views.blogpost, name='newblog'),
]