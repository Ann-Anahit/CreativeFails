
from django.urls import path
from .views import register_view, index_view

urlpatterns = [
path('register/', register_view, name='register'),
path('', index_view, name='index'),
]