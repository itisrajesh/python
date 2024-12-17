from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'accounts/home.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/accounts/success' + '?username=' + user.username + '&email=' + user.email)
        else:
            messages.info(request, 'Username or Password is incorrect')
    return render(request, 'accounts/login.html')


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(username, email, password)
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exists')
            return render(request, 'accounts/register.html')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email already exists')
            return render(request, 'accounts/register.html')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return render(request, 'accounts/login.html')
    return render(request, 'accounts/register.html')


@login_required(login_url='/accounts/login')
def success_page(request):
    username = request.GET.get('username')
    email = request.GET.get('email')
    return render(request, 'accounts/success.html', {'username': username, 'email': email})


def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/accounts')
    else :
        messages.info(request, 'You are not logged in')
        return redirect('/accounts')