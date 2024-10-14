from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import like_post, unlike_post



urlpatterns = [
    path('', views.home_view, name='home'),
    path('posts/', views.post_list_view, name='post_list'),
    path('write/', views.write_article_view, name='write_article'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),  
    path('<int:post_id>/', views.post_detail_view, name='post_detail'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('<int:post_id>/comment/', views.add_comment_view, name='add_comment'),
    path('comments/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('comments/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('posts/<int:post_id>/like/', like_post, name='like_post'),
    path('posts/<int:post_id>/unlike/', unlike_post, name='unlike_post'),
]
