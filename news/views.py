from django.shortcuts import render
from .models import News

def home(request):
    news_list = News.objects.all().order_by('-created_at')
    return render(request, 'news/home.html', {'news_list': news_list})
