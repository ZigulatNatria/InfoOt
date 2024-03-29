from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserAddView, logout_view

urlpatterns = [
    path('login/',
         LoginView.as_view(template_name = 'sign/login.html'),
         name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/',
         UserAddView.as_view(template_name='sign/signup.html'),
         name='signup'),
]