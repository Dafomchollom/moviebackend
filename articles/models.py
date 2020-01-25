from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absoulte_url(self):
        return reverse('list_of_post_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Star(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(default='default.png', blank=True)
    poster = models.ImageField(default='defaultstar.png', blank=True)
    about = models.TextField(blank=True, default='no information')

    class Meta:
        ordering = ('name',)
        verbose_name = 'star'
        verbose_name_plural = 'stars'

    def get_absoulte_url(self):
        return reverse('list_of_post_by_star', args=[self.slug])

    def __str__(self):
        return self.name

    def snippet(self):
        return self.about[:300] + '...'

class Director(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(default='default.png', blank=True)
    poster = models.ImageField(default='defaultstar.png', blank=True)
    about = models.TextField(blank=True, default='no information')

    class Meta:
        ordering = ('name',)
        verbose_name = 'director'
        verbose_name_plural = 'directors'

    def get_absoulte_url(self):
        return reverse('list_of_post_by_director', args=[self.slug])

    def __str__(self):
        return self.name


 
class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    movie_name = models.CharField(max_length=300, blank=True)
    title = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True)
    category = models.ManyToManyField(Category)
    # star = models.ManyToManyField(Star, default='none')
    # director = models.ManyToManyField(Director, default='none')
    thumbnail = models.ImageField(default='default.png',blank=True)
    poster = models.ImageField(default='defaultposter.png', blank=True)
    summary = RichTextUploadingField(default='no information',blank=True)
    body = RichTextUploadingField()
    # rating = models.IntegerField(default='0', blank=True)
    releasedate = models.DateField()
    dateseen = models.DateField()
    postdate = models.DateField()
    # editorspick = models.BooleanField(default=False)
    # classic = models.BooleanField(default=False)
    # in_cinema = models.BooleanField(default=False)
    Post_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:1000]

    def snippet2(self):
        return self.body[:30]

    def snippet3(self):
        return self.summary[:300] + '...'

    def snippetmobile(self):
        return self.summary[:100] + '...'


class Comment(models.Model):
    STATUS_CHOICES = (
        ('block', 'Block'),
        ('published', 'Published'),
    )
    post = models.ForeignKey(Article, related_name='comments')
    user = models.CharField(max_length=250)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    comment_status = models.BooleanField(default=False)

    def approved(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.user


class Advert(models.Model):
    ADVERT_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    name = models.CharField(max_length=500)
    image = models.ImageField()
    link = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    Advert_status = models.CharField(max_length=10, choices=ADVERT_CHOICES, default='draft')

    def __str__(self):
        return self.name
