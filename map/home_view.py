from django.shortcuts import render
from .models import Post

def home_view(request):
    published_posts = Post.objects.filter(published=True) 
    context = {'published_posts': published_posts}
    return render(request, 'index.html', context)