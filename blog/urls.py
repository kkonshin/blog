from django.conf.urls import url
from . import views
from .feeds import LatestPostsFeed

# Порядок урлов очень важен. Понять.

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^feed/$', LatestPostsFeed(), name='post_feed'),
    url(r'^(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
]