from django.shortcuts import render, get_object_or_404

from .models import News


def index(request):
    new = News.objects.all()

    return render(request, 'article/news.html', context={'new': new})


def new_detail(request, id):
    new = get_object_or_404(News, id=id)
    return render(request, 'article/new.html', context={"new": new})
