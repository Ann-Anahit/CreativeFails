from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list_view, name='post_list'),
    path('my-posts/', views.user_posts, name='user_posts'),
    path('write/', views.write_article_view, name='write_article'),
    path('posts/edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('<int:post_id>/', views.post_detail_view, name='post_detail'),
    path('posts/delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('<int:post_id>/comment/', views.add_comment_view, name='add_comment'),
    path('comments/edit/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('comments/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('post/<int:post_id>/like/', views.post_like, name='post_like'),  
    path('post/<int:post_id>/unlike/', views.post_unlike, name='post_unlike'),
    path('delete-image/<int:post_id>/', views.delete_image, name='delete_image'),
]
