from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.models import Article


def index_view(request: WSGIRequest):
    articles = Article.objects.exclude(is_deleted=True)
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context=context)
