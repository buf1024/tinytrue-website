from django.conf.urls import patterns, include, url

import tinytrue

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tinytrue.views.home', name='home'),
    # url(r'^tinytrue/', include('tinytrue.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if tinytrue.settings.DEBUG:
	urlpatterns += patterns('tinylog.views_debug',
		url(r'^test/header$', 'test_view_header'),
		url(r'^test/footer$', 'test_view_footer'),
		url(r'^test/passage$', 'test_view_passage'),
		url(r'^test/passagecount$', 'test_view_passagecount'),
	)