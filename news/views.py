from django.shortcuts import render
from .models import Article
from django.views.generic import ListView


def news_home(request):
    news = Article.objects.order_by('date') # сортировка
    return render(request, 'news/news_home.html', {'news': news})
# Create your views here.

def create(request):
    return render(request, 'news/create.html')
