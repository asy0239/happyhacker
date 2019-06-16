from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


def signup(request):
    if request.method == 'POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)  ## request 자체도 넣어 줘야함
        if form.is_valid():
            auth_login(request, form.get_user())   ## 로그인을 함
            return redirect('posts:index')
    else:
        form = AuthenticationForm()   ## 인증하는 작업
    return render(request, 'accounts/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('posts:index')


