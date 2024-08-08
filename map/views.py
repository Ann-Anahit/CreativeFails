from django.shortcuts import render, redirect  
from django.contrib.auth.models import User  
from .forms import RegistrationForm  
from django.conf import settings  
from django.shortcuts import render 
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def profile_view(request):
    user = request.user  
    return render(request, 'profile.html', {'user': user})

def home_view(request):  
    return render(request, 'map/home.html')  

def login_view(request):
    return render(request, 'accounts/login.html')  

def logout_view(request):
    logout(request)
    return redirect('map/home') 

def register_view(request):  
    if request.method == 'POST':  
        form = RegistrationForm(request.POST)  
        if form.is_valid():  
           
            user = form.save(commit=False)  
            user.set_password(form.cleaned_data['password'])  
            user.save()  
            return redirect('home')   
    else:  
        form = RegistrationForm()  

  
    return render(request, 'accounts/register.html', {'form': form})

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)