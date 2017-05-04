from django.http import Http404
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


def archives(requset):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(requset, 'archives.html', {'post_list': post_list, 'error': False})


def about_me(request):
    return render(request, 'aboutme.html')


def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category__exact=tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list': post_list, 'error': True})
