from datetime import datetime
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

from article.models import Article


def home(requset):
    post_list = Article.objects.all()
    return render(requset, 'home.html', {'post_list': post_list})


def detail(requset, my_args):
    return HttpResponse("hello,world %s" % my_args)
