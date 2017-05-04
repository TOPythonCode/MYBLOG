from django.contrib.syndication.views import Feed
from django.http import Http404
from django.shortcuts import render, redirect
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

from article.models import Article


def home(requset):
    post_list = Article.objects.all()
    paginator = Paginator(post_list,2)
    page = requset.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.paginator(paginator.num_pages)
    return render(requset, 'home.html', {'post_list': posts})


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


def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'home.html')
        else:
            post_list = Article.objects.filter(title__icontains=s)
            if len(post_list) == 0:
                return render(request, 'archives.html', {'post_list': post_list, 'error': True})
            else:
                return render(request, 'archives.html', {'post_list': post_list, 'error': False})

    return redirect('/')


class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.date_time

    def item_description(self, item):
        return item.content
