from django.shortcuts import render, get_object_or_404, redirect  
from django.contrib.auth.decorators import login_required  
from django.contrib.auth import logout  
from django.http import HttpResponseForbidden  
from django.contrib import messages  
from .models import Post, Comment  
from .forms import PostForm, CommentForm  

@login_required
def post_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user.is_authenticated:
        post.likes.add(request.user)
    return redirect('post_detail', post_id=post.id)

@login_required
def post_unlike(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user.is_authenticated:
        post.likes.remove(request.user)
    return redirect('post_detail', post_id=post.id)

@login_required
def home_view(request):  
    """View for the homepage, showing all posts or a sign-up prompt."""
    posts = Post.objects.prefetch_related('comments').all()
    is_authenticated = request.user.is_authenticated  # Check if the user is authenticated

    return render(request, 'map/home.html', {
        'posts': posts,
        'is_authenticated': is_authenticated,
    })
@login_required
def write_article_view(request, post_id=None):
    """View for creating or editing posts."""
    post = None
    if post_id:  # Editing an existing post
        post = get_object_or_404(Post, id=post_id)
        if post.user != request.user:  # Ensure the post belongs to the logged-in user
            return HttpResponseForbidden("You can only edit your own posts.")

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
def post_list_view(request):
    """View to list all posts."""
    posts = Post.objects.all()  # Retrieve all posts from the database
    for post in posts:
        # Check if the current user has liked each post
        post.is_liked = post.likes.filter(id=request.user.id).exists()
    
    context = {
        'posts': posts,  # Pass the posts to the template
    }
    
    return render(request, 'map/home.html', context)  # Pass the full context
 

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
def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post has been updated successfully!')
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})

@login_required  
def delete_post(request, post_id):  
    """View to delete a post."""  
    post = get_object_or_404(Post, pk=post_id)  
    if post.user != request.user:
        return HttpResponseForbidden("You can only delete your own posts.")  
    
    if request.method == 'POST':  
        post.delete()  
        messages.success(request, 'Your post has been deleted successfully!')  
        return redirect('home')  
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
        content = request.POST.get('content')
        form = CommentForm(request.POST)  
        if form.is_valid():  
            comment = form.save(commit=False)  
            comment.post = post  
            comment.user = request.user   
            comment.save()  
            messages.success(request, 'Your comment has been added successfully!')  
            return redirect('post_detail', post_id=post.id)  
    else:  
        form = CommentForm()  
    
    # For rendering the post details and the comment form  
    return render(request, 'posts/post_detail.html', {'post': post, 'comment_form': form})

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your comment has been updated successfully!')
            return redirect('post_detail', post_id=comment.post.id)  
    else:
        form = CommentForm(instance=comment)

    return render(request, 'comments/edit_comment.html', {'form': form, 'comment': comment})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == "POST":
        comment.delete()
        messages.success(request, 'Your comment has been deleted successfully!')
        return redirect('post_detail', post_id=comment.post.id) 

    return render(request, 'comments/delete_comment.html', {'comment': comment})


