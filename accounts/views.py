from django.shortcuts import render, redirect  
from django.contrib.auth import login, authenticate, logout  
from django.contrib.auth.forms import AuthenticationForm  
from django.contrib.auth.decorators import login_required   
from .forms import CustomUserCreationForm  

def register(request):  
    if request.method == 'POST':  
        form = CustomUserCreationForm(request.POST)  # Use your custom form here  
        if form.is_valid():  
            user = form.save()  # Save the new user  
            login(request, user)  # Automatically log in the user after creation  
            return redirect('index')  # Redirect to the index or any destination  
    else:  
        form = CustomUserCreationForm()  # Create a blank form instance  

    return render(request, 'accounts/register.html', {'form': form})  # Update the template path if necessary  

def login_view(request):  
    if request.method == 'POST':  
        form = AuthenticationForm(data=request.POST)  
        if form.is_valid():  
            user = form.get_user()  
            login(request, user)  
            return redirect('index')  
    else:  
        form = AuthenticationForm()  
    return render(request, 'login.html', {'form': form})   

@login_required   
def profile_view(request):  
    user = request.user  
    return render(request, 'profiles.html', {'user': user})   

def logout_view(request):  
    logout(request)  
    return redirect('index')