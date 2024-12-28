from django.shortcuts import render, redirect
from posts.models import Post
from django.core.paginator import Paginator
from django.db.models import Count

def home_view(request):
    top_3_posts = Post.objects.annotate(num_comments=Count('comments')).order_by('-num_comments')[:3]
    other_posts = Post.objects.annotate(num_comments=Count('comments')).order_by('-num_comments')[3:]
    paginator = Paginator(other_posts, 3)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'map/home.html', {
        'top_3_posts': top_3_posts,
        'page_obj': page_obj,
    })

def about_view(request):
    return render(request, 'map/about.html')

def custom_404_view(request, exception):
    return render(request, 'map/404.html', status=404)
