from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import Post, Matzip_list
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    query = request.GET.get('search', '')
    group = Matzip_list.objects.filter(address__contains=query)
    num_pages = 10
    paginator = Paginator(group, num_pages)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    group_list = []
    store_names = []
    menu = []
    images = []
    for gp in group:
        group_list.append(gp)
    for gp in group:
        store_names.append(gp.store_name)
    for gp in group:
        menu.append(gp.Menu.split('\n'))
    for gp in group:
        images.append(gp.images_url.split('\n'))
    store_menus = dict(zip(store_names, menu))

    context = {
        'query': query,
        'store_menus': store_menus,
        'images': images,
        'contacts': contacts,
    }
    return render(request, 'posts/lists.html', context)



def mypage(request):
    return render(request, 'posts/mypage.html')


def detail(request):
    return render(request, 'posts/detail.html')







