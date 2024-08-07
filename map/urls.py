from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
]  

handler404 = 'map.views.custom_404_view'