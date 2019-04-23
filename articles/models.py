from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
# Create your models here.

class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=1000)
    slug = models.SlugField()
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