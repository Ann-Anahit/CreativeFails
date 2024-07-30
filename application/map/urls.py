
from django.urls import path
from django.contrib import admin
from . import views
from .views import register_view, index_view  
from map import views

urlpatterns = [
path('admin/', admin.site.urls),
path('register/', register_view, name='register'),  
path('', index_view, name='index'),
]
