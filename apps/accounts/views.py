from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser or user.is_master:
                login(request, user)
                return redirect('master_dashboard')
    return render(request, 'auth/login.html')


def logout_view(reqest):
    logout(reqest)
    return redirect('login')
