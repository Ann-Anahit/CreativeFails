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
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)  # This should be present in your model
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    featured_image = models.ImageField(upload_to='featured_images/', blank=True, null=True)
    
    def __str__(self):
        return self.title 

class Comment(models.Model):  
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")  
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    content = models.TextField()  
    created_at = models.DateTimeField(default=timezone.now)  

    def __str__(self):  
        return f"Comment by {self.user.username} on post {self.post.id}"