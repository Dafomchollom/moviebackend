from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(default='default.png',blank=True)
    body = RichTextUploadingField()
    releasedate = models.DateField()
    dateseen = models.DateField()
    postdate = models.DateTimeField(default=timezone.now)
    Post_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:1000]

    def snippet2(self):
        return self.body[:30]