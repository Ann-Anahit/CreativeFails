from django.contrib.auth.decorators import login_required

@login_required
def write_article_view(request):
    if request.method == 'POST':
        form = WriteArticleForm(request.POST, request.FILES)  # Assuming a WriteArticleForm
        if form.is_valid():
            # Get the currently logged-in user
            user = request.user
            # Set the user for the form's instance
            form.instance.user = user
            post = form.save()
            # ... other logic
            return redirect('some_success_view')
    else:
        form = WriteArticleForm()

    return render(request, 'posts/write_article.html', {'form': form})