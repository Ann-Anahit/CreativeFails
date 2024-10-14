from django.db import models  
from django.utils import timezone  
from accounts.models import CustomUser  
from django.core.validators import MaxLengthValidator  
from cloudinary.models import CloudinaryField  
from django.contrib.auth.models import User 
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)  # Add this line

    def __str__(self):
        return self.title

class Comment(models.Model):  
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")  
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    content = models.TextField()  
    created_at = models.DateTimeField(default=timezone.now)  

    def __str__(self):  
        return f"Comment by {self.user.username} on post {self.post.id}"