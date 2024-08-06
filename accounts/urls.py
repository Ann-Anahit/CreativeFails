from django.urls import path  
from . import views  
from django.contrib.auth import views as auth_views 
from .views import CustomLoginView, register_view, login_view, profile_view, logout_view 

urlpatterns = [  
    path('register/', views.register_view, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),   
    path('logout/', views.logout_view, name='logout'),       
    path('profile/', views.profile_view, name='profile'),      
]