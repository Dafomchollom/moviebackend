from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
# Create your views here.
def articlehome(request):
    article = Article.objects.all().filter(Post_status='published').order_by('-postdate')[:3]
    carousel = Article.objects.all().filter(Post_status='published').order_by('-postdate')[:5]
    return render(request, 'articles/home.html', {'article': article, 'carousel':carousel})

def articleDetails(request, slug):
    articles = Article.objects.get(slug=slug)
    return render(request, 'articles/view.html', {'articles':articles})