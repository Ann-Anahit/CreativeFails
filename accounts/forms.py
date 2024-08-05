from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm  
from .models import CustomUser
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class RegistrationForm(forms.ModelForm):
        def clean_password(self):
            password = self.cleaned_data.get('password')
            if len(password) < 6:
                raise ValidationError('Password must be at least 6 characters long')
            return password
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email address already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        return user

    class CustomUserChangeForm(UserChangeForm):
        class Meta:
            model = CustomUser
            exclude = ('password',) 