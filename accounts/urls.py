from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import register_view, custom_login, logout_view

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('accounts/login/', views.custom_login, name='login'), 
    path('accounts/logout/', views.logout_view, name='logout'),
]
