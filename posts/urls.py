from django.urls import path  
from . import views  

urlpatterns = [  
    path('', views.post_list_view, name='index'),                     # List all posts  
    path('create/', views.create_post_view, name='create_post'),          # Create a new post 
    path('write_article/', views.write_article_view, name='write_article'),  # Write article page 
    path('<int:post_id>/', views.post_detail_view, name='post_detail'),    # View a single post  
    path('<int:post_id>/edit/', views.update_post_view, name='update_post'),  # Edit a post  
    path('<int:post_id>/delete/', views.delete_post_view, name='delete_post'), # Delete a post  
] 