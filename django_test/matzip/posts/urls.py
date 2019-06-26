from django.urls import path, include
from . import views

app_name = 'posts'


urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('main/', views.main, name='main'),
    path('lists/', views.lists, name='lists'),
    path('mypage/', views.mypage, name='mypage'),
    path('detail/', views.detail, name='detail'),
]
