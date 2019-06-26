from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, 'posts/index.html')


def all(request):
    return render(request, 'posts/index.html')


def search(request):
    return render(request, 'posts/search.html')


def star(request):
    return render(request, 'posts/star.html')


def test(request):
    return render(request, 'posts/test.html')


def main(request):
    return render(request, 'posts/main.html')


def lists(request):
    return render(request, 'posts/lists.html')


def mypage(request):
    return render(request, 'posts/mypage.html')


def detail(request):
    return render(request, 'posts/detail.html')







