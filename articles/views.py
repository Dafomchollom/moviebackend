from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Category, Advert, Star, Director
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from .forms import CommentForm
# Create your views here.
def list_of_post_by_category(request, category_slug):
    categories = Category.objects.all()
    adverts = Advert.objects.all().filter(Advert_status='published').order_by('-date')[:2]
    postAds = Article.objects.filter(Post_status='published').order_by('-postdate')
    post = Article.objects.filter(Post_status='published').order_by('-postdate')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        post = post.filter(category=category).order_by('-postdate')
        postAds = post.filter(category=category).order_by('-postdate')[:3]
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
    paginator = Paginator (article, 3)
    page = request.GET.get('page')
    try : 
        posts = paginator.page(page)
    except PageNotAnInteger :
        posts = paginator.page(1)
    except EmptyPage :
        posts = paginator.page(paginator.num_pages)
    return render(request, 'articles/home.html', {'posts': posts,'page': page,'article': article, 'articleAds': articleAds, 'carousel':carousel, 'adverts': adverts, 'classic':classic, 'editor':editor})

def articleDetails(request, slug):
    articleAds = Article.objects.all().filter(Post_status='published').order_by('-postdate')[:3]
    adverts = Advert.objects.all().filter(Advert_status='published').order_by('-date')
    post = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        form =  CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('details', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'articles/view.html', {'post':post,'adverts': adverts})

def search(request):
    template = 'articles/search.html'

    query = request.GET.get('q')

    results = Article.objects.filter(Q(title__icontains=query) | Q(movie_name__icontains=query) | Q(body__icontains=query)| Q(title__iexact=query) | Q(movie_name__iexact=query) | Q(body__iexact=query)).order_by('-movie_name')

    context = {'results':results, 'query' : query}

    return render(request, template, context)