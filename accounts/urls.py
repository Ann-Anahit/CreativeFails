from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import register_view, CustomLoginView, profile_view, logout_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('accounts/login/', custom_login, name='login'),
    path('accounts/profile/', views.profile_view, name='profile'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  
]