from rest_framework import serializers
from .models import Profile, FailedProject, Comment

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class FailedProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = FailedProject
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment 
        fields = '__all__'