from django.urls import path, include
from . import views


app_name = 'testapp'



urlpatterns = [
    # main
    path('main/', views.index, name='main'),
    path('<int:article_id>/', views.detail, name='detail'),
    # create
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    # delete

]