from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from truck_auth.forms import LoginForm, RegisterForm, UserProfileForm
from truck_auth.models import UserProfile


def login_user(request):
    if request.method == 'GET':
        context = {
            'form': LoginForm(),
            'page_name': 'login page'
        }
        return render(request, 'user/login.html', context)
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home page')
        context = {
            'form': form,
        }
        return render(request, 'user/login.html', context)


def register_user(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm(),
            'page_name': 'register page',
        }
        return render(request, 'user/register.html', context)
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile(user=user)
            profile.save()
            login(request, user)
            return redirect('home page')
        context = {
            'form': form,
            'page_name': 'register page',
        }
        return render(request, 'user/register.html', context)


@login_required
def logout_user(request):
    if request.method == 'GET':
        context = {
            'page_name': 'logout page',
        }
        return render(request, 'user/logout.html', context)
    else:
        logout(request)
        return redirect('home page')


@login_required
def profile_user(request):
    if request.method == 'GET':
        context = {
            'profile': request.user.userprofile,
            'trucks': request.user.truck_set.all().order_by('-id'),
            'form': UserProfileForm(instance=request.user.userprofile),
            'page_name': 'profile page',
        }
        return render(request, 'user/profile.html', context)
    else:
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile user')
        context = {
            'profile': request.user.userprofile,
            'trucks': request.user.truck_set.all().order_by('-id'),
            'form': form,
            'page_name': 'profile page',
        }
        return render(request, 'user/profile.html', context)
