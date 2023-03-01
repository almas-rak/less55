from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse


from webapp.models import Article, StatusChoice


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'article_create.html', context={'choices': StatusChoice.choices})
    article_data = {
        'title': request.POST.get('title'),
        'text': request.POST.get('text'),
        'author': request.POST.get('author'),
        'status': request.POST.get('status')
    }
    article = Article.objects.create(**article_data)

    return redirect('article_detail', pk=article.pk)


def detail_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article.html', context={
        'article': article,

    })


def update_view(request: WSGIRequest, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.author = request.POST.get('author')
        article.text = request.POST.get('text')
        article.status = request.POST.get('status')
        article.save()
        return redirect('article_detail', pk=article.pk)
    return render(request, 'article_update.html', 
                  context={
                    'article': article,
                    'choices': StatusChoice.choices
                  })


def delete_view(request: WSGIRequest, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_confirm_delete.html', context={'article': article})


def confirm_delete(request: WSGIRequest, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('index')

    
