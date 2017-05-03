from datetime import datetime
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render


def home(requset):
    return HttpResponse("hello world, Django")


def detail(requset, my_args):
    return HttpResponse("hello,world %s" % my_args)


def test(requset):
    return render(requset, 'test.html', {'current_time': datetime.now()})
