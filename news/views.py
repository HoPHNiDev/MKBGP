from django.shortcuts import render
from django.core import serializers
from .models import Articles, ArticleViewersData
from django.http import HttpResponse
from django.views.generic import View, DetailView
from ipware import get_client_ip


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


class ArticlesHome(View):
    def get(self, request):
        if is_ajax(request):
            x = request.GET.get('value', 5)
            if Articles.objects.order_by('-id').count() - (int(x) + 5) >= 0:
                y = int(x) + 5
            else:
                y = Articles.objects.order_by('-id').count()
            data = serializers.serialize(
                'json', Articles.objects.filter(status=True).order_by('-id')[int(x):int(y)])
            return HttpResponse(data, content_type='application/json')

        else:
            news = Articles.objects.filter(status=True).order_by('-id')[0:5]
            news_count = Articles.objects.filter(
                status=True).order_by('-id').count()
            news_status = news_count > 5
            return render(request, 'news/news.html', {'news': news, 'count': news_count, 'news_status': news_status})


class ArticlesView(View):

    def get(self, request, slug):
        ip, is_routable = get_client_ip(request)
        if request.path.split('/')[1] == 'en':
            urlSlug = request.path.replace('/en/news/', '')
        else:
            urlSlug = request.path.replace('/ru/news/', '')
        article = Articles.objects.get(
            slug=urlSlug)
        if ip != None:
            if ArticleViewersData.objects.filter(article=article).filter(ip_address=ip).exists():
                pass
            else:
                ArticleViewersData.objects.create(
                    article=article, ip_address=ip)
                article.views += 1
                article.save()

        return render(request, 'news/news_detail.html', {'article': article})
