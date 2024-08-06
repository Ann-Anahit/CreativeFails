from django.shortcuts import render, redirect  
from django.contrib.auth import login, logout, authenticate  
from django.contrib.auth.forms import AuthenticationForm  
from django.contrib.auth.decorators import login_required  
from .forms import CustomUserCreationForm  
from django.contrib.auth.signals import user_logged_in 
from django.contrib.auth.views import LoginView   
from django.contrib import messages  
from .models import CustomUser

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
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):  
    if request.method == "POST":  
        form = AuthenticationForm(data=request.POST)  
        if form.is_valid():  
            username = form.cleaned_data.get('username')  
            password = form.cleaned_data.get('password')  
            user = authenticate(request, username=username, password=password)  
            if user is not None:  
                login(request, user)  
                return redirect('home')  # Redirect after successful login  
            else:  
                messages.error(request, "Invalid username or password.")  
        else:  
            messages.error(request, "Please correct the errors below.")  
    else:  
        form = AuthenticationForm()  

    return render(request, 'accounts/registration/login.html', {'form': form})  

class CustomLoginView(LoginView):  
    template_name = 'accounts/registration/login.html'

@login_required  
def profile_view(request):  
    user = request.user  
    return render(request, 'accounts/profile.html', {'user': user})  

def logout_view(request):  
    logout(request)  
    return redirect('home') 