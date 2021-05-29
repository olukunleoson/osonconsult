from django.contrib import admin
from django.urls import path, include
from blogpage import views

urlpatterns = [
    path('blog/', views.blog_page, name='blog'),

]
