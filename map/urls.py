from django.urls import path  
from . import views  
from .home_views import home_view


urlpatterns = [  
    path("", views.home_view, name="home"),    
    path("register/", views.register_view, name="register"),  
]