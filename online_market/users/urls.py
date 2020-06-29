from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from online_market.users.views import (
    register, profile_contacts, profile_address, orders
)

app_name = 'users'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(
        template_name='login.html', redirect_authenticated_user=True
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile_contacts/', profile_contacts, name='profile_contacts'),
    path('profile_address/', profile_address, name='profile_address'),
    path('orders/', orders, name='orders'),
]
