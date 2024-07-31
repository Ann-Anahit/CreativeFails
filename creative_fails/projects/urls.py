# projects/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, FailedProjectViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'failedprojects', FailedProjectViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]