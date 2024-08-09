from django.contrib import admin  
from django.urls import path, include  
from accounts import views as account_views  
from django.contrib.auth import views as auth_views  
from . import views
from .views import register_view, CustomLoginView, profile_view, logout_view

  

urlpatterns = [  
    path("admin/", admin.site.urls),  
    path("", include("map.urls")),  
    path("register/", account_views.register_view, name="register"),  
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  
    path("accounts/", include("django.contrib.auth.urls")),  
    path("posts/", include("posts.urls")),  
    path('accounts/profile/', views.profile_view, name='profile'),
]