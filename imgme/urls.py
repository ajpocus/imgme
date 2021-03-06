from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'imgme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^accounts/', include('allauth.urls')),

    url(r'^$', 'imgbase.views.home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth$', 'imgbase.views.auth'),
    url(r'^auth/granted', 'imgbase.views.granted')
)
