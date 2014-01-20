from django.conf.urls import patterns, url

from photos import views
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<poll_id>\d+)/score/$', views.score, name='score'),
)
