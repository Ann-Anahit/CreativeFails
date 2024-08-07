from django.shortcuts import render, get_object_or_404, redirect  
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post  
from .forms import PostForm 

@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Your post has been created successfully!')
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'posts/write_article.html', {'form': form})

def home_view(request):
    posts = Post.objects.all()
    return render(request, 'map/home.html', {'posts': posts})

def post_list_view(request):  
    posts = Post.objects.all()  
    return render(request, 'posts/post_list.html', {'posts': posts})  

def post_detail_view(request, post_id):  
    post = get_object_or_404(Post, id=post_id)  
    return render(request, 'posts/post_detail.html', {'post': post})  

@login_required
def update_post_view(request, post_id):  
    post = get_object_or_404(Post, id=post_id)  
    if request.method == 'POST':  
        form = PostForm(request.POST, instance=post)  
        if form.is_valid():  
            form.save()  
            messages.success(request, 'Your post has been updated successfully!')
            return redirect('post_detail', post_id=post.id)  
    else:  
        form = PostForm(instance=post)  
    return render(request, 'posts/post_form.html', {'form': form})  

@login_required
def delete_post_view(request, post_id):  
    post = get_object_or_404(Post, id=post_id)  
    if request.method == 'POST':  
        post.delete()  
        messages.success(request, 'Your post has been deleted successfully!')
        return redirect('post_list')  
    return render(request, 'posts/post_confirm_delete.html', {'post': post})  
