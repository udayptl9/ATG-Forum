from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as auth_reg_views
urlpatterns = [
    path('authers/register/', auth_reg_views.register, name='register'),
    path('', auth_reg_views.home, name='authers_home'),
    path('authers/login/',
         auth_views.LoginView.as_view(template_name='authers/login.html'), name='login'),
    path('authers/logout/', auth_views.LogoutView.as_view(template_name='authers/logout.html'), name='logout'),
]
