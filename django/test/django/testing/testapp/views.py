from django.shortcuts import render, redirect
from .models import Articles
# Create your views here.


def index(request):
    articles = Articles.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'testapp/index.html', context)


def detail(request, article_id):
    article = Articles.objects.get(id=article_id)
    print(article)
    context = {
        'article': article
    }
    return render(request, 'testapp/detail.html', context)


def new(request):
    return render(request, 'testapp/new.html')


def create(request):
    if request.method == 'POST':
        article = Articles()
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('testapp:main')
    else:
        return render(request, 'testapp/new.html')




