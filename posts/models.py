from django.db import models  
from django.utils import timezone  
from accounts.models import CustomUser

class Post(models.Model):  
    title = models.CharField(max_length=200)  
    content = models.TextField()  
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    created_at = models.DateTimeField(auto_now_add=True)  
    visibility = models.BooleanField(default=True)  

    def __str__(self):  
        return self.title  

class Comment(models.Model):  
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")  
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    content = models.TextField()  
    created_at = models.DateTimeField(default=timezone.now) 
     
    def __str__(self):  
        return f"Comment by {self.user.username} on post {self.post.id}"
