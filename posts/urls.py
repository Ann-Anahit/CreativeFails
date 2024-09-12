from django.urls import path  
from . import views  
from .views import custom_logout_view  

urlpatterns = [  
    path('', views.home_view, name='home'),  
    path('posts/', views.post_list_view, name='post_list'),  
    path('posts/write/', views.create_post_view, name='write_article'), 
    path('posts/<int:post_id>/', views.post_detail_view, name='post_detail'),  
    path('posts/<int:post_id>/edit/', views.update_post_view, name='edit_post'),  
    path('posts/<int:post_id>/delete/', views.delete_post_view, name='delete_post'),   
    path('posts/<int:post_id>/comment/', views.add_comment_view, name='add_comment'),  
    path('logout/', custom_logout_view, name='logout'),  
]