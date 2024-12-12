from django.urls import path, include
from django.contrib import admin
from accounts import views as account_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("map.urls")),
    path("register/", account_views.register_view, name="register"),
    path('accounts/login/', account_views.custom_login, name='login'),  
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("accounts/profile/", account_views.profile_view, name="profile"),
    path("posts/", include("posts.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'map.views.custom_404_view'