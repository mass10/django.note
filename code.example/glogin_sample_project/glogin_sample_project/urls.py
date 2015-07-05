# coding: utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin
import glogin_sample_app

admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	url(r'^$', 'glogin_sample_app.views.index', name='index'),
	# url(r'^blog/', include('blog.urls')),
	url(r'^glogin', 'glogin_sample_app.views.glogin'),

	url(r'^admin/', include(admin.site.urls)),
	# url(r'^glogin/', 'glogin_sample_project.views.glogin'),
)
