from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.articlehome),
    url(r'^(?P<slug>[\w-]+)/$', views.articleDetails, name="details"),
]
