from django.contrib import admin
from .models import Article, Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class Articles_admin(admin.ModelAdmin):
    list_display = ('id','title','postdate','Post_status')
    list_filter = ('Post_status','postdate')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Article, Articles_admin)    