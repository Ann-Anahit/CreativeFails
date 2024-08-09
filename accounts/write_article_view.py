from django.contrib.auth.decorators import login_required
from django import forms
from .models import Post

@login_required
def write_article_view(request):
    if request.method == 'POST':
        form =PostForm(request.POST) 
        if form.is_valid():
            post = form.save(commit=False)  
            post.user = request.user  
            post.save() 
      
    else:
        form = PostForm()

    return render(request, 'posts/write_article.html', {'form': form})