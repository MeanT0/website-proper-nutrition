from django.shortcuts import render, redirect
from .models import Article
from django.views.generic import ListView
from datetime import datetime


def news_home(request):
    news = Article.objects.order_by('-date') # сортировка по убыванию
    return render(request, 'news/news_home.html', {'news': news})
# Create your views here.

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        full_text = request.POST.get('full_text')
        date_str = request.POST.get('date')
        
        # Parse the datetime string
        try:
            date = datetime.fromisoformat(date_str)
        except (ValueError, TypeError):
            date = datetime.now()
        
        article = Article(
            title=title,
            full_text=full_text,
            date=date
        )
        article.save()
        return redirect('news_home')
    
    return render(request, 'news/create.html')
