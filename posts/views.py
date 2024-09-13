from django.shortcuts import render, get_object_or_404, redirect  
from django.contrib.auth.decorators import login_required  
from django.contrib.auth import logout  
from django.http import HttpResponseForbidden  
from django.contrib import messages  
from .models import Post, Comment  
from .forms import PostForm, CommentForm  

@login_required
def create_post_view(request):
    """View to create a new post."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  
            post.save()
            messages.success(request, 'Your post has been created successfully!')
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form, 'post': None})


def home_view(request):  
    """View for the homepage, showing all posts."""  
    posts = Post.objects.all()  
    return render(request, 'map/home.html', {'posts': posts})  

def post_list_view(request):  
    """View to list all posts."""  
    posts = Post.objects.all()  
    return render(request, 'map/home.html', {'posts': posts})  

def post_detail_view(request, post_id):  
    """View to display a single post's details."""  
    post = get_object_or_404(Post, id=post_id) 
    is_owner = request.user == post.user  
    return render(request, 'posts/post_detail.html', {'post': post, 'is_owner': is_owner})  

@login_required
def update_post_view(request, post_id):
    """View to update an existing post."""
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.user:  
        return HttpResponseForbidden("You can only edit your own posts.")
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post has been updated successfully!')
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form, 'post': post})

@login_required  
def delete_post_view(request, post_id):  
    """View to delete a post."""  
    post = get_object_or_404(Post, id=post_id)  
    if request.user != post.author:  # assuming 'author' is the field name  
        return HttpResponseForbidden("You can only delete your own posts.")  
    
    if request.method == 'POST':  
        post.delete()  
        messages.success(request, 'Your post has been deleted successfully!')  
        return redirect('post_list')  
    return render(request, 'posts/confirm_delete.html', {'post': post})  

@login_required  
def custom_logout_view(request):  
    """Logout the user and redirect to home."""  
    logout(request)  
    return redirect('home')  

@login_required  
def add_comment_view(request, post_id):  
    """View to add a comment to a post."""  
    post = get_object_or_404(Post, id=post_id)  
    
    if request.method == 'POST':  
        form = CommentForm(request.POST)  
        if form.is_valid():  
            comment = form.save(commit=False)  
            comment.post = post  
            comment.user = request.user  # assuming 'user' is the field name in Comment model  
            comment.save()  
            messages.success(request, 'Your comment has been added successfully!')  
            return redirect('post_detail', post_id=post.id)  
    else:  
        form = CommentForm()  
    
    # For rendering the post details and the comment form  
    return render(request, 'posts/post_detail.html', {'post': post, 'comment_form': form})