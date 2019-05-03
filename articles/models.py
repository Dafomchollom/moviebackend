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
 
class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True)
    category = models.ManyToManyField(Category)
    thumbnail = models.ImageField(default='default.png',blank=True)
    body = RichTextUploadingField()
    releasedate = models.DateField()
    dateseen = models.DateField()
    postdate = models.DateField()
    Post_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:1000]

    def snippet2(self):
        return self.body[:30]


class Comment(models.Model):
    post = models.ForeignKey(Article, related_name='comments')
    user = models.CharField(max_length=250)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def approved(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.user