from django.shortcuts import render, get_object_or_404, redirect  
from django.contrib.auth.decorators import login_required  
from django.contrib.auth import logout  
from django.http import HttpResponseForbidden  
from django.contrib import messages  
from .models import Post, Comment  
from .forms import PostForm, CommentForm  

@login_required
def write_article_view(request, post_id=None):
    """View for creating or editing posts."""
    if post_id:  # Editing an existing post
        post = get_object_or_404(Post, id=post_id)
        if post.user != request.user:  # Ensure the post belongs to the logged-in user
            return HttpResponseForbidden("You can only edit your own posts.")
    else:  # Creating a new post
        post = None

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            new_post = form.save(commit=False)  # Don't save to the DB yet
            new_post.user = request.user  # Set the user field to the logged-in user
            new_post.save()  # Now save to the DB
            messages.success(request, 'Your post has been saved successfully!')
            return redirect('post_list')  # Redirect to post list after saving
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/write_article.html', {'form': form, 'post': post})

@login_required
def home_view(request):  
    """View for the homepage, showing all posts."""  
    posts = Post.objects.all()  
    return render(request, 'map/home.html', {'posts': posts})  

@login_required
def post_list_view(request):  
    """View to list all posts."""  
    posts = Post.objects.all()  
    return render(request, 'map/home.html', {'posts': posts})  

@login_required
def post_detail_view(request, post_id):
    """View to display a single post's details."""
    post = get_object_or_404(Post, id=post_id)
    print(f"Post: {post.title}, Image: {post.image}") 
    is_owner = request.user == post.user
    comments = Comment.objects.filter(post=post)    
    liked = post.likes.filter(id=request.user.id).exists()  
    return render(request, 'posts/post_detail.html', {
        'post': post,
        'is_owner': is_owner,
        'comments': comments,
        'liked': liked,
        'comment_form': CommentForm(),
    })

@login_required
def edit_post(request, pk):
    """View to edit a post."""
    post = get_object_or_404(Post, pk=pk)
    if post.user != request.user:
        return HttpResponseForbidden("You can only edit your own posts.")

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post has been updated successfully!')
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})

@login_required  
def delete_post(request, pk):  
    """View to delete a post."""  
    post = get_object_or_404(Post, pk=pk)  
    if post.user != request.user:
        return HttpResponseForbidden("You can only delete your own posts.")  
    
    if request.method == 'POST':  
        post.delete()  
        messages.success(request, 'Your post has been deleted successfully!')  
        return redirect('post_list')  
    return render(request, 'posts/delete_post.html', {'post': post})  

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

@login_required
def post_like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('post_detail', slug=slug)