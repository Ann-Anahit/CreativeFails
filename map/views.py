from django.shortcuts import render, redirect  
from django.contrib.auth.models import User  
from django.contrib.auth import login  
from django.contrib import messages  

def register_view(request):  
    if request.method == 'POST':  
        username = request.POST['username']  
        email = request.POST['email']  
        password = request.POST['password']  
        confirm_password = request.POST['confirm-password']  

        if password == confirm_password:  
            if User.objects.filter(username=username).exists():  
                messages.error(request, 'Username already exists')  
            elif User.objects.filter(email=email).exists():  
                messages.error(request, 'Email already exists')  
            else:  
                user = User.objects.create_user(username=username, email=email, password=password)  
                user.save()  
                login(request, user)  
                messages.success(request, 'You have registered successfully')  
                return redirect('/')  # Redirect to a landing page or homepage.  
        else:  
            messages.error(request, 'Passwords do not match')  
            
    return render(request, 'map/register.html')  

def index_view(request):  
    return render(request, 'map/index.html')  