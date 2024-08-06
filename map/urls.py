from django.urls import path  
from .views import home_view, custom_404_view  

urlpatterns = [  
    path('', home_view, name='home'),  
]  

handler404 = custom_404_view