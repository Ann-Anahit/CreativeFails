from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    """Form for creating a new user."""
    
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'artist')  # Removed email field

    def clean_username(self):
        """Check if the username already exists."""
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError("Username already exists.")
        return username

    def clean_password1(self):
        """Ensure the password meets minimum length requirements."""
        password = self.cleaned_data.get('password1')
        if password and len(password) < 6:
            raise ValidationError('Your password must contain at least 6 characters.')
        return password 

    def clean_aritst(self):
        artist = self.cleaned_data.get('artist')
        return artist

class CustomUserChangeForm(UserChangeForm):
    """Form for updating an existing user."""
    
    class Meta:
        model = CustomUser
        fields = ('username',)  # Specify fields you want to change
