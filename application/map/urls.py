
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
  
    path('register/', views.register_view, name='register'),
    path("", TemplateView.as_view(template_name="map/index.html"), name="index"),
]
