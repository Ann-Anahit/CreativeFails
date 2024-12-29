from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'learned_lessons', 'category']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
