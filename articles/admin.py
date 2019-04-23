from django.contrib import admin
from .models import Article, Category
# Register your models here.
class Articles_admin(admin.ModelAdmin):
    list_display = ('id','title','postdate','Post_status')
    list_filter = ('Post_status','postdate')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Article, Articles_admin)

class category_admin(admin.ModelAdmin):
    list_display = ('id','name','slug',)
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, category_admin)