from django.shortcuts import render, get_object_or_404

from .models import News


def index(request):
    news = News.objects.all()

    return render(request, 'article/news.html', context={'news': news})
