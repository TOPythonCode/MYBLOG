from datetime import datetime

from django.http import Http404
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

from article.models import Article


def home(requset):
    post_list = Article.objects.all()
    return render(requset, 'home.html', {'post_list': post_list})


def detail(requset, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(requset, 'post.html', {'post': post})
