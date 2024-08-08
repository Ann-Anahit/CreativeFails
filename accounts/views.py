from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import CustomUser


class CustomLoginView(LoginView):  
    template_name = 'accounts/login.html' 

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1'] 

            user = CustomUser.objects.create_user(
                email=email,
                username=username,
                password=password
            )
            login(request, user)
            return redirect('map/home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def custom_login(request):  
    if request.method == 'POST':  
        form = AuthenticationForm(data=request.POST)  
        if form.is_valid():  
            username = form.cleaned_data.get('username')  
            password = form.cleaned_data.get('password')  
            user = authenticate(request, username=username, password=password)  
            if user is not None:  
                login(request, user)  
                return redirect('map/home')   
    else:  
        form = AuthenticationForm()  
    return render(request, 'accounts/login.html', {'form': form})  

@login_required  
def profile_view(request):  
    user = request.user  
    return render(request, 'accounts/profile.html', {'user': user})  

def logout_view(request):  
    logout(request)  
    return redirect('map/home')
