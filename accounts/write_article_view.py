from django.contrib.auth.decorators import login_required
from django import forms
from .models import Post

@login_required
def write_article_view(request):
    if request.method == 'POST':
        form =PostForm(request.POST) 
        if form.is_valid():
            post = form.save(commit=False)  # Don't save immediately
            post.user = request.user  # Assign the logged-in user
            post.save()  # Now save the post with the assigned user
            # ... other success logic ...
    else:
        form = PostForm()

    return render(request, 'posts/write_article.html', {'form': form})