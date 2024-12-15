from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from posts.models import Post

def profile_view(request):
    user = request.user  
    posts = Post.objects.prefetch_related('comments').all()
    return render(request, 'accounts/profile.html', {'user': user})

def home_view(request):  
    posts = Post.objects.prefetch_related('comments').all()
    is_authenticated = request.user.is_authenticated

    print(f"Total Posts: {len(posts)}")
    for post in posts:
        print(f"Post: {post.title}, Comments: {post.comments.count()}")

    sorted_posts = sorted(posts, key=lambda post: post.comments.count(), reverse=True)

    top_3_posts = sorted_posts[:3]
    print(f"Top 3 Posts: {[post.title for post in top_3_posts]}")

    return render(request, 'map/home.html', {
        'top_3_posts': top_3_posts,
        'is_authenticated': is_authenticated,
    })
def login_view(request):
    """Redirect authenticated users away from the login page."""
    if request.user.is_authenticated:
        return redirect('home') 
    
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('home') 

def register_view(request):  
    if request.method == 'POST':  
        form = RegistrationForm(request.POST)  
        if form.is_valid():  
            user = form.save(commit=False)  
            user.set_password(form.cleaned_data['password'])  
            user.save()  
            return redirect('home')   
    else:  
        form = RegistrationForm()  

    return render(request, 'accounts/register.html', {'form': form})

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
