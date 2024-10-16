from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import post_like, post_unlike



urlpatterns = [
    path('', views.home_view, name='home'),
    path('posts/', views.post_list_view, name='post_list'),
    path('write/', views.write_article_view, name='write_article'),
    path('posts/edit/<int:post_id>/', views.edit_post, name='edit_post'),  
    path('<int:post_id>/', views.post_detail_view, name='post_detail'),
    path('posts/delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('<int:post_id>/comment/', views.add_comment_view, name='add_comment'),
    path('comments/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('comments/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('like<int:post_id>/', post_like, name='post_like'),
    path('unlike/<int:post_id>/', post_unlike, name='post_unlike'),
]
