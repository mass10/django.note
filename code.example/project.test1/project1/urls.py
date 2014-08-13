# coding: utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

	# Examples:
	# url(r'^$', 'project1.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^$', 'app1.views.main', name='main'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^api$', 'app1.views.api', name='api'),
	url(r'^login$', 'app1.views.login', name='login'),
	url(r'^logout$', 'app1.views.logout', name='logout'),
	url(r'^filters/$', 'app1.filters.views.show', name='show'),
	url(r'^filters/show$', 'app1.filters.views.show', name='show'),
	url(r'^listeners/$', 'app1.listeners.views.show', name='show'),
	url(r'^listeners/show$', 'app1.listeners.views.show', name='show'),
	url(r'^users/$', 'app1.users.views.show', name='show'),
	url(r'^users/show$', 'app1.users.views.show', name='show'),
	url(r'^users/add$', 'app1.users.views.add', name='add'),
	url(r'^users/add_complete$', 'app1.users.views.add_complete', name=''),
	url(r'^users/del$', 'app1.users.views.del', name='del'),
)
