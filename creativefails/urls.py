from django.urls import path, include
from map.views import home_view
from accounts import views as account_views
from map.views import about_view

urlpatterns = [
    path('', home_view, name='home'),
    path("register/", account_views.register_view, name="register"),
    path('accounts/login/', account_views.custom_login, name='login'),
    path('accounts/logout/', account_views.logout_view, name='logout'),
    path("posts/", include("posts.urls")),
    path('about/', about_view, name='about'),
]
