from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.articlehome),
    url(r'^(?P<slug>[\w-]+)/$', views.articleDetails, name="details"),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.list_of_post_by_category, name='list_of_post_by_category'),
    url(r'^star/(?P<star_slug>[-\w]+)/$', views.list_of_post_by_star, name='list_of_post_by_star'),
    url(r'^director/(?P<director_slug>[-\w]+)/$', views.list_of_post_by_director, name='list_of_post_by_director'),
]
