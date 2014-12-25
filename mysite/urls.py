from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('data.urls')),
#    url(r'^data/', include('data.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
