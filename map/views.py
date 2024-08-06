from django.shortcuts import render, redirect  
from django.contrib.auth.models import User  
from .forms import RegistrationForm  
from django.conf import settings  
from django.shortcuts import render 
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def profile_view(request):
    user = request.user  # Assuming you're using Django's auth system
    # Additional logic to fetch profile data if needed
    return render(request, 'profile.html', {'user': user})

def home_view(request):  
    return render(request, 'map/home.html')  

def login_view(request):
    # Your login logic here (e.g., handling authentication forms, etc.)
    return render(request, 'login.html')  # Replace with your login template name

def logout_view(request):
    logout(request)  # Log the user out using Django's logout function
    return render(request, 'logout.html')  # Redirect to a logout confirmation page (optional)

def register_view(request):  
    if request.method == 'POST':  
        form = RegistrationForm(request.POST)  
        if form.is_valid():  
            # Create and save the new user  
            user = form.save(commit=False)  
            user.set_password(form.cleaned_data['password'])  # Hash the password  
            user.save()  
            return redirect('home')  # Redirect after successful registration  
    else:  
        form = RegistrationForm()  

    # Update the template path to the accounts app  
    return render(request, 'accounts/register.html', {'form': form})

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)