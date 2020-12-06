from django.urls import path

from truck_auth.views import login_user, logout_user, register_user, profile_user

urlpatterns = [
    path('login/', login_user, name="login user"),
    path('logout/', logout_user, name="logout user"),
    path('register/', register_user, name="register user"),
    path('profile/', profile_user, name='profile user'),
]
