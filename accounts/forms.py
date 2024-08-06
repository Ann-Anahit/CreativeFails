from django import forms  
from django.contrib.auth.forms import UserCreationForm, UserChangeForm  
from .models import CustomUser  
from django.core.exceptions import ValidationError  


class CustomUserCreationForm(UserCreationForm):  
    email = forms.EmailField(required=True)  

    class Meta:  
        model = CustomUser  
        fields = ('username', 'email', 'password1', 'password2')  
        error_messages = {  
            'username': {  
                'required': 'Username is required.',  
                'max_length': 'Username is too long.',  
            },  
        }  
        
    def clean_username(self):  
        username = self.cleaned_data.get('username')  
        if CustomUser.objects.filter(username=username).exists():  
            raise ValidationError("Username already exists.")  
        return username  

    def clean_email(self):  
        email = self.cleaned_data.get('email')  
        if CustomUser.objects.filter(email=email).exists():  
            raise ValidationError("Email address already exists.")  
        return email  
    
    def clean_password1(self):  
        password = self.cleaned_data.get('password1')  
        username = self.cleaned_data.get('username')  
        email = self.cleaned_data.get('email')  

        # Password length validation  
        if len(password) < 6:  
            raise ValidationError('Your password must contain at least 6 characters.') 

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