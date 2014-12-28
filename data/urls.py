from django.conf.urls import patterns, url
from django.conf import settings
from data import views

urlpatterns = patterns('',
    url(r'^$', views.index,name='index')
   ) 


if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
