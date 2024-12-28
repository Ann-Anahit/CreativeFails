from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import register_view, CustomLoginView, logout_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('accounts/login/', custom_login, name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  
]