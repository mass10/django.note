# coding: utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin
import app1
from app1.gview01.views import *
from app1.gview02.views import *

admin.autodiscover()

# app1.gview01.views.gview01()

urlpatterns = patterns('',

	# Examples:
	# url(r'^$', 'project1.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^$', 'app1.views.default', name='default'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^api$', 'app1.views.api', name='api'),
	url(r'^login$', 'app1.views.login', name='login'),
	url(r'^logout$', 'app1.views.logout', name='logout'),
	url(r'^filters/$', 'app1.filters.views.show', name='show'),
	url(r'^filters/show$', 'app1.filters.views.show', name='show'),
	url(r'^listeners/$', 'app1.listeners.views.show', name='show'),
	url(r'^listeners/show$', 'app1.listeners.views.show', name='show'),
	url(r'^xusers/$', 'app1.xusers.views.show', name='show'),
	url(r'^xusers/show$', 'app1.xusers.views.show', name='show'),
	url(r'^xusers/add$', 'app1.xusers.views.add', name='add'),
	url(r'^xusers/add_complete$', 'app1.xusers.views.add_complete', name=''),
	url(r'^chat/$', 'app1.chat.views.default', name=''),
	url(r'^top/$', 'app1.top.views.show', name='show'),
	url(r'^floatings/$', 'app1.floatings.views.default', name='show'),
	url(r'^gview01/$', gview01.as_view()),
	url(r'^gview02/$', gview02.as_view()),
)
