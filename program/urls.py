from django.contrib import admin
from django.urls import path, include
from program import views


urlpatterns = [
    path('programs/', views.program, name='programs'),
    path('iskilld/', views.iskilld, name='iskilld'),
    path('cyt/', views.cyt, name='cyt'),
    path('Nleague/', views.Nations_league, name='iskilld'),

    
    ]