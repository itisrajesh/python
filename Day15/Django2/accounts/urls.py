from django.urls import path
from .views import home , login_page, register_page, logout_page, success_page

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_page, name='logout'),
    path('success/', success_page, name='success'),
]
