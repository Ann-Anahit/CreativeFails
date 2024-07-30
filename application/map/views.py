
from django.shortcuts import render

def register_view(request):
    if request.method == 'POST':
        # Logik für POST-Anfragen
        pass
    return render(request, 'register.html')
