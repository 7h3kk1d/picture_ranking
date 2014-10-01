from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
import settings
admin.autodiscover()

from picture_ranking import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'picture_ranking.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', 'picture_ranking.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^',include('photos.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
