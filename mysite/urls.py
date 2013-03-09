from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls')),     # polls application
    url(r'^admin/', include(admin.site.urls)),  # admin
)
