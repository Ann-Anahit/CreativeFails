from django.shortcuts import render, get_object_or_404, redirect  
from django.contrib.auth.decorators import login_required  
from django.http import HttpResponseForbidden  
from django.contrib import messages  
from .models import Post, Comment  
from .forms import PostForm, CommentForm  


@login_required
def post_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        messages.success(request, "You unliked the post.")
    else:
        post.likes.add(request.user)
        messages.success(request, "You liked the post.")
    return redirect('post_detail', post_id=post.id)

@login_required
def post_unlike(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        messages.success(request, "You unliked the post.")
    return redirect('post_detail', post_id=post.id)

@login_required
def write_article_view(request, post_id=None):
    """View for creating or editing posts."""
    post = None
    if post_id:
        post = get_object_or_404(Post, id=post_id)
        if post.user != request.user:
            return HttpResponseForbidden("You can only edit your own posts.")

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            messages.success(request, "Your post has been saved successfully!")
            return redirect('user_posts')
    else:
        form = PostForm(instance=post)

    if not request.user.is_artist:
        messages.error(request, "You must be an artist to access this page.")
        return redirect('home')

    return render(request, 'posts/write_article.html', {'form': form, 'post': post})

@login_required
def post_list_view(request):
    """View to list all posts."""
    posts = Post.objects.all().order_by('-created_at')
    for post in posts:
        post.is_liked = post.likes.filter(id=request.user.id).exists()
    
    context = {
        'posts': posts,
    }
    
    return render(request, 'map/home.html', context) 

@login_required
def user_posts(request):
    if not request.user.is_artist:
        messages.error(request, "You must be an artist to access this page.")
        return redirect('home')
    
    user_posts = Post.objects.filter(user=request.user).order_by('-created_at')
    total_posts = user_posts.count()
    total_comments = Comment.objects.filter(post__in=user_posts).count()
    total_likes = sum(post.likes.count() for post in user_posts)

    return render(request, 'posts/user_posts.html', {
        'posts': user_posts,
        'total_posts': total_posts,
        'total_comments': total_comments,
        'total_likes': total_likes,
    })

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
            messages.success(request, "Your post has been updated successfully!")
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.user != request.user:
        messages.error(request, "You are not authorized to delete this post.")
        return redirect('post_detail', post_id=post.id)

    if request.method == 'POST':
        post.delete()
        messages.success(request, "The post has been deleted successfully!")
        return redirect('user_posts')

    return render(request, 'posts/delete_post.html', {'post': post})

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
            messages.success(request, "Your comment has been added successfully!")
            return redirect('post_detail', post_id=post.id)
    else:  
        form = CommentForm()  
    
    return render(request, 'posts/post_detail.html', {'post': post, 'comment_form': form})

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Your comment has been updated successfully!")
            return redirect('post_detail', post_id=comment.post.id)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'comments/edit_comment.html', {'form': form, 'comment': comment})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post = comment.post

    if post.user != request.user and comment.user != request.user:
        messages.error(request, "You are not authorized to delete this comment.")
        return redirect('post_detail', post_id=post.id)

    if request.method == "POST":
        comment.delete()
        messages.success(request, "The comment has been deleted successfully!")
        return redirect('post_detail', post_id=post.id)

    return render(request, 'comments/delete_comment.html', {'comment': comment, 'post': post})
