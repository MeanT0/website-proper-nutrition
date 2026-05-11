from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.views.generic import ListView
from datetime import datetime


def news_home(request):
    news = Article.objects.order_by('-date') # сортировка по убыванию
    return render(request, 'news/news_home.html', {'news': news})

def news_detail(request, id):
    news = get_object_or_404(Article, pk=id)
    return render(request, 'news/news_detail.html', {'news': news})
# Create your views here.

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        anons = request.POST.get('anons')
        full_text = request.POST.get('full_text')
        date_str = request.POST.get('date')
        
        # Parse the datetime string
        try:
            date = datetime.fromisoformat(date_str)
        except (ValueError, TypeError):
            date = datetime.now()
        
        article = Article(
            title=title,
            anons=anons,
            full_text=full_text,
            date=date
        )
        article.save()
        return redirect('news_home')
    
    return render(request, 'news/create.html')
