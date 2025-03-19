from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('home/', views.home , name='home'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:pk>/',views.edit_task, name='edit'),
    path('delete/<int:pk>/',views.delete_task, name='delete'),
    
]
