from django.contrib import admin
from .models import Article, Category, Comment, Advert,Star, Director
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

# class StarsAdmin(admin.ModelAdmin):
#     list_display = ('name', 'slug')
#     prepopulated_fields = {'slug': ('name',)}
# admin.site.register(Star, StarsAdmin)

# class DirectorAdmin(admin.ModelAdmin):
#     list_display = ('name', 'slug')
#     prepopulated_fields = {'slug': ('name',)}
# admin.site.register(Director, DirectorAdmin)

class Articles_admin(admin.ModelAdmin):
    list_display = ('id','movie_name','title','postdate','Post_status')
    list_filter = ('Post_status','postdate')
    search_fields = ('movie_name','title', 'body')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Article, Articles_admin)  

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'comment_status', 'post')
    list_filter = ('comment_status','post')
admin.site.register(Comment, CommentAdmin)

class AdvertsAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'Advert_status')
admin.site.register(Advert, AdvertsAdmin)