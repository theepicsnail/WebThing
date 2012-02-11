from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from UplinkThing.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WebThing.views.home', name='home'),
    # url(r'^WebThing/', include('WebThing.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin',      include(admin.site.urls)),
    url(r'^logout',     logout),
    url(r'^ajax',       ajax),
    url(r'^login',      login),
    url(r'^register',   register),
    url(r'^index',      index),
    url(r'^profile$',   profileLookup),
    url(r'^profile/(?P<name>.*)$',profile),
    url(r'^computer/(?P<cid>.*)/(?P<action>.*)$',   computer),
    url(r'^upgrade$',   upgrade),
    url(r'^terminal$',  terminal),
    url(r'^$',          index)
)
