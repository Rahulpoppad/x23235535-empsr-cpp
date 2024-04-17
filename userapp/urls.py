from django.urls import path, include
from userapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='log.html'), name='login'),
    path('logout/', views.logout, name='logout'),
    path('password_reset/', include('django.contrib.auth.urls')),  # Include Django's password reset URLs
    # Add other custom URL patterns as needed
]
