from django.urls import path
from .views import register_view, CustomLoginView, profile_view, logout_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
]