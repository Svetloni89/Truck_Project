from django.urls import path

from .views import *

urlpatterns = [
    path('login/', login_user, name="login user"),
    path('logout/', logout_user, name="logout user"),
    path('register/', register_user, name="register user"),
    path('profile/', profile_user, name='profile user'),
]
