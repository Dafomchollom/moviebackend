from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Advert, Star, Director
from django.http import HttpResponse
# Create your views here.
def list_of_post_by_category(request, category_slug):
    categories = Category.objects.all()
    adverts = Advert.objects.all().filter(Advert_status='published').order_by('-date')[:2]
    postAds = Article.objects.filter(Post_status='published').order_by('-postdate')
    post = Article.objects.filter(Post_status='published').order_by('-postdate')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        post = post.filter(category=category).order_by('-postdate')
        postAds = post.filter(category=category).order_by('-postdate')[:2]
    template = 'articles/category-home.html'
    context = { 'categories':categories, 'post': post, 'postAds': postAds, 'category': category,'adverts': adverts}
    return render(request, template, context)

def list_of_post_by_star(request, star_slug):
    stars = Star.objects.all()
    post = Article.objects.filter(Post_status='published').order_by('-postdate')
    postAds = Article.objects.filter(Post_status='published').order_by('-postdate')
    if star_slug:
        star = get_object_or_404(Star, slug=star_slug)
        post = post.filter(star=star).order_by('-postdate')
        postAds = post.filter(star=star).order_by('-postdate')[:3]
    template = 'articles/stars-home.html'
    context = {'stars':stars, 'post': post, 'postAds': postAds, 'star': star}
    return render(request, template, context)

def list_of_post_by_director(request, director_slug):
    directors = Star.objects.all()
    post = Article.objects.filter(Post_status='published').order_by('-postdate')
    postAds = Article.objects.filter(Post_status='published').order_by('-postdate')
    if director_slug:
        director = get_object_or_404(Director, slug=director_slug)
        post = post.filter(director=director).order_by('-postdate')
        postAds = post.filter(director=director).order_by('-postdate')[:3]
    template = 'articles/directors.html'
    context = {'directors':directors, 'post': post, 'postAds': postAds, 'director': director}
    return render(request, template, context)

def articlehome(request):
    article = Article.objects.all().filter(Post_status='published').order_by('-postdate')
    articleAds = Article.objects.all().filter(Post_status='published').order_by('-postdate')[:2]
    carousel = Article.objects.all().filter(Post_status='published').order_by('-postdate')[:4]
    adverts = Advert.objects.all().filter(Advert_status='published').order_by('-date')
    classic = Article.objects.filter(classic=True).order_by('-postdate')[:4]
    editor = Article.objects.filter(editorspick=True).order_by('-postdate')[:4]
    return render(request, 'articles/home.html', {'article': article, 'articleAds': articleAds, 'carousel':carousel, 'adverts': adverts, 'classic':classic, 'editor':editor})

def articleDetails(request, slug):
    articles = Article.objects.get(slug=slug)
    articleAds = Article.objects.all().filter(Post_status='published').order_by('-postdate')[:3]
    adverts = Advert.objects.all().filter(Advert_status='published').order_by('-date')
    return render(request, 'articles/view.html', {'articles':articles,'adverts': adverts})