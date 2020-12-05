from django.urls import path

from truck_auth.views import login_user, logout_user, register_user, profile_user

urlpatterns = [
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('register/', register_user, name="register"),
    path('profile/', profile_user, name='profile'),
]
