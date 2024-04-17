from django.urls import path, include
from userapp import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('password_reset/', include('django.contrib.auth.urls')),  # Include Django's password reset URLs
    # Add other custom URL patterns as needed
]
