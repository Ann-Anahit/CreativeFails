from django.db import models
from django.contrib.auth.models import User

# Create models.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

class FailedProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fitle = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    failed_project = models.ForeignKey(FailedProject, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)