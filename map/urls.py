from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]  

handler404 = 'map.views.custom_404_view'