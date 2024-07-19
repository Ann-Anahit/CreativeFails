from django.shortcuts import render

from rest_framework import viewsets
from .models import Profile, FailedProject, Comment
from .serializers import ProfileSerializer, FailedProjectSerializer, CommentSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class FailedProjectViewSet(viewsets.ModelViewSet):
    queryset = FailedProject.objects.all()
    serializer_class = FailedProjectSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer