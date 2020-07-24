from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='jonblog'),
    url(r'^blog/(?P<page>\d+)$', views.blog, name='archive'),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog/(?P<slug>.*)$', views.post, name='blog_post'),
]
