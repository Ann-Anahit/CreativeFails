from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),  # Registration path
    path('login/', views.login_view, name='login'),           # Login path
    path('logout/', views.logout_view, name='logout'),        # Logout path
    path('profile/', views.profile_view, name='profile'),     # Profile view path
]