from django.urls import path  
from . import views  
from django.contrib.auth import views as auth_views 

urlpatterns = [  
    path('register/', views.register_view, name='register'),  
    path('logout/', views.logout_view, name='logout'),       
    path('profile/', views.profile_view, name='profile'),      
]