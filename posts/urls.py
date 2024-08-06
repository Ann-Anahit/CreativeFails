from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('posts/', views.post_list_view, name='post_list'),
    path('posts/<int:post_id>/', views.post_detail_view, name='post_detail'),
    path('posts/write/', views.create_post_view, name='write_article'),
    path('posts/update/<int:post_id>/', views.update_post_view, name='update_post'),
    path('posts/delete/<int:post_id>/', views.delete_post_view, name='delete_post'),
]