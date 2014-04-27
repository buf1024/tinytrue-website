# coding: utf-8
from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

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

    url(r'^$', 'tinylog.views.home'),
    url(r'^install$', 'tinylog.views.install'),
    url(r'^manage$', 'tinylog.views.admin'),
    url(r'^manage/admin$', 'tinylog.views.admin'),
    url(r'^manage/passage$', 'tinylog.views.mngpassage'),
    url(r'^manage/comment$', 'tinylog.views.mngcomment'),
    url(r'^manage/catalog$', 'tinylog.views.mngcatalog'),
    url(r'^manage/label$', 'tinylog.views.mnglabel'),
    url(r'^manage/setting$', 'tinylog.views.mngsetting'),
    url(r'^manage/game$', 'tinylog.views.mnggame'),
    )

if tinytrue.settings.DEBUG:
    urlpatterns += patterns('tinylog.views_debug',
        url(r'^test/header$', 'test_view_header'),
        url(r'^test/footer$', 'test_view_footer'),
        url(r'^test/passage$', 'test_view_passage'),
        url(r'^test/passagecount$', 'test_view_passagecount'),
        url(r'^test/gameitem$', 'test_view_gameitem'),
    )

    #静态文件
    urlpatterns += patterns('',
        url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT + '/js'}),
        url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT + '/css'}),
        url(r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT + '/img'}),
        )
    