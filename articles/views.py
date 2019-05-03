from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from django.http import HttpResponse
# Create your views here.
def list_of_post_by_category(request, category_slug):
    categories = Category.objects.all()
    post = Article.objects.filter(Post_status='published')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        post = post.filter(category=category)
    template = 'articles/category-home.html'
    context = {'categories':categories, 'post': post, 'category': category}
    return render(request, template, context)

def articlehome(request):
    article = Article.objects.all().filter(Post_status='published').order_by('-postdate')[:3]
    carousel = Article.objects.all().filter(Post_status='published').order_by('-postdate')[:4]
    return render(request, 'articles/home.html', {'article': article, 'carousel':carousel})

def articleDetails(request, slug):
    articles = Article.objects.get(slug=slug)
    return render(request, 'articles/view.html', {'articles':articles})