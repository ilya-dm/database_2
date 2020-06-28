from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    news = Article.objects.prefetch_related('scopes').order_by(ordering)
    context = {'news': news}


    return render(request, template, context)
