from django.shortcuts import render, redirect  
from django.contrib.auth import login, authenticate  
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  

def register(request):  
    if request.method == 'POST':  
        form = UserCreationForm(request.POST)  
        if form.is_valid():  
            form.save()  
            username = form.cleaned_data.get('username')  
            password = form.cleaned_data.get('password1')  
            user = authenticate(username=username, password=password)  
            login(request, user)  
            return redirect('home')  
    else:  
        form = UserCreationForm()  
    return render(request, 'register.html', {'form': form})  

def login_view(request):  
    if request.method == 'POST':  
        form = AuthenticationForm(data=request.POST)  
        if form.is_valid():  
            user = form.get_user()  
            login(request, user)  
            return redirect('home')  
    else:  
        form = AuthenticationForm()  
    return render(request, 'login.html', {'form': form})  

def logout_view(request):  
    from django.contrib.auth import logout  
    logout(request)  
    return redirect('home')  