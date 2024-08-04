from django.shortcuts import render, redirect  
from django.contrib.auth.models import User  
from .forms import RegistrationForm  
from django.conf import settings  

def index_view(request):  
    return render(request, 'map/index.html')  

def register_view(request):  
    if request.method == 'POST':  
        form = RegistrationForm(request.POST)  
        if form.is_valid():  
            # Create and save the new user  
            user = form.save(commit=False)  
            user.set_password(form.cleaned_data['password'])  # Hash the password  
            user.save()  
            return redirect('index')  # Redirect after successful registration  
    else:  
        form = RegistrationForm()  

    # Update the template path to the accounts app  
    return render(request, 'accounts/register.html', {'form': form})