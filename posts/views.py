from django.shortcuts import render, get_object_or_404, redirect  
from .models import Post  
from .forms import PostForm 
from django.views import generic 

@login_required
def write_article_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title, content=content, author=request.user)
        messages.success(request, 'Your post has been created successfully!')
        return redirect('index')
    return render(request, 'posts/write_article.html')

def post_list_view(request):  
    posts = Post.objects.all()  
    return render(request, 'posts/post_list.html', {'posts': posts})  

def post_detail_view(request, post_id):  
    post = get_object_or_404(Post, id=post_id)  
    return render(request, 'posts/post_detail.html', {'post': post})  

def create_post_view(request):  
    if request.method == 'POST':  
        form = PostForm(request.POST)  
        if form.is_valid():  
            post = form.save(commit=False)  
            post.author = request.user    
            post.save()  
            return redirect('post_list')  
    else:  
        form = PostForm()  
    return render(request, 'posts/post_form.html', {'form': form})  

def update_post_view(request, post_id):  
    post = get_object_or_404(Post, id=post_id)  
    if request.method == 'POST':  
        form = PostForm(request.POST, instance=post)  
        if form.is_valid():  
            form.save()  
            return redirect('post_detail', post_id=post.id)  
    else:  
        form = PostForm(instance=post)  
    return render(request, 'posts/post_form.html', {'form': form})  

def delete_post_view(request, post_id):  
    post = get_object_or_404(Post, id=post_id)  
    if request.method == 'POST':  
        post.delete()  
        return redirect('post_list')  
    return render(request, 'posts/post_confirm_delete.html', {'post': post})  
