from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
 
urlpatterns = [
    # authentication urls
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),

    path('signup/', views.signup, name='signup'),
    # normal urls
    path('', views.home , name='home'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:pk>/',views.edit_task, name='edit'),
    path('delete/<int:pk>/',views.delete_task, name='delete'),
    path('complete/<int:pk>/', views.completed, name = 'complete'),
    # path('login/',views.login, name='login')
    # path('checkbox')
    
]
 