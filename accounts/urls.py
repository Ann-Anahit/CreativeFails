from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view, CustomLoginView, profile_view, logout_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'), 
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
]