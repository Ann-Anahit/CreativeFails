from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.core.paginator import Paginator


def home_view(request):
    top_3_posts = Post.objects.annotate(num_comments=Count('comments')).order_by('-num_comments')[:3]
    
    other_posts = Post.objects.annotate(num_comments=Count('comments')).order_by('-num_comments')[3:]
    
    paginator = Paginator(other_posts, 3)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'home.html', {
        'top_3_posts': top_3_posts,
        'page_obj': page_obj,
    })

def profile_view(request):
    user = request.user  
    posts = Post.objects.prefetch_related('comments').all()
    return render(request, 'accounts/profile.html', {'user': user})


def about_view(request):
    return render(request, 'map/about.html')

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
