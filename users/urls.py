from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserProfileView
from allauth.account.views import SignupView
app_name = 'users'

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', SignupView.as_view(template_name='users/register.html'), name='register'),
]
