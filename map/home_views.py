from django.shortcuts import render
from posts.models import Post

def home_view(request):
    posts = Post.objects.all()
    return render(request, 'map/home.html', {'posts': posts})
