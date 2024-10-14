from django.urls import path, include 
from . import views  

urlpatterns = [  
    path('', views.home_view, name='home'),  
    path('posts/', views.post_list_view, name='post_list'), 
    path('posts/write/', views.write_article_view, name='write_article'), 
    path('edit/<int:pk>/', views.edit_post, name='edit_post'),
    path('posts/<int:post_id>/', views.post_detail_view, name='post_detail'),  
    path('posts/delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('posts/<int:post_id>/comment/', views.add_comment_view, name='add_comment'),  
    path('logout/', views.custom_logout_view, name='logout'),  
]
