
from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import register_view, index_view  

urlpatterns = [
path('admin/', admin.site.urls),
path('register/', register_view, name='register'),  
path('', index_view, name='index'),
]
