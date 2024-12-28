from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about')
]  

handler404 = 'map.views.custom_404_view'