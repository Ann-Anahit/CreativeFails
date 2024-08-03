from django.urls import path  
from . import views  

urlpatterns = [  
    path('', views.post_list_view, name='post_list'),           # List of posts  
    path('create/', views.create_post_view, name='create_post'), # Create a new post  
    path('<int:post_id>/', views.post_detail_view, name='post_detail'), # Detail of a specific post  
]