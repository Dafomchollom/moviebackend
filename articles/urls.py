from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.articlehome, name="home"),
    url(r'^results/$', views.search, name="search"),
    url(r'^classic/$', views.classic, name="classic"),
    url(r'^starslist/$', views.starlist, name="starlist"),
    url(r'^editor/$', views.editor, name="editor"),
    url(r'^(?P<slug>[\w-]+)/$', views.articleDetails, name="details"),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.list_of_post_by_category, name='list_of_post_by_category'),
    url(r'^star/(?P<star_slug>[-\w]+)/$', views.list_of_post_by_star, name='list_of_post_by_star'),
    url(r'^director/(?P<director_slug>[-\w]+)/$', views.list_of_post_by_director, name='list_of_post_by_director'),
]
