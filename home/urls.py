from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    
]