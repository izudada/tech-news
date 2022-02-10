from django.http import HttpResponse
from django.shortcuts import render

from .tasks import  published_news

# Create your views here.
def test(request):
    # test_func.delay()
    published_news.delay()
    return HttpResponse('Done')