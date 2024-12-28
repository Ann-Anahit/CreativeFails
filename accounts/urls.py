from django.urls import path
from . import views 

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('accounts/login/', views.custom_login, name='login'), 
    path('accounts/logout/', views.logout_view, name='logout'),
]
