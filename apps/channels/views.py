from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def master_home_page(request):
    return render(request, 'master/index.html')
