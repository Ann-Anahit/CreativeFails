from django.urls import path
from django.views.generic.base import TemplateView
from hello_world import views as index_views

from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="map/index.html"), name="index")
]