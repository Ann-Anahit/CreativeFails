from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')), 
    path('', include('map.urls')), 
    path('posts/', include('posts.urls')), 
]
