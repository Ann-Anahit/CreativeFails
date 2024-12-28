from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('', views.home_view, name='homepage'),
    path('about/', views.about_view, name='about'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'), 
]  

handler404 = 'map.views.custom_404_view'