# coding: utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin
import app1
from app1.top.views import *
from app1.gview01.views import *
from app1.gview02.views import *
from app1.images.views import *

admin.autodiscover()

urlpatterns = patterns('',

	# Examples:
	# url(r'^$', 'project1.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	# ROOT
	url(r'^$', 'app1.views.default', name='default'),

	# 組み込みの管理画面
	url(r'^admin/', include(admin.site.urls)),

	# Web API のサンプル
	url(r'^api$', 'app1.views.api', name='api'),

	# チャット画面の練習
	url(r'^chat/$', 'app1.chat.views.default', name=''),
	url(r'^chat/messages$', 'app1.chat.views.messages', name=''),

	# HTML のイベント練習
	url(r'^events/$', 'app1.events.views.default'),

	# iptables の状況表示
	url(r'^filters/$', 'app1.filters.views.show', name='show'),
	url(r'^filters/show$', 'app1.filters.views.show'),
	url(r'^filters/content$', 'app1.filters.views.content'),

	# リキッドレイアウト風の練習
	url(r'^floatings/$', 'app1.floatings.views.default', name='show'),
	url(r'^floatings/time$', 'app1.floatings.views.time', name=''),

	# template view を使用した view の練習
	url(r'^gview01/$', gview01.as_view()),
	url(r'^gview02/$', gview02.as_view()),

	# netstat の状況を表示
	url(r'^listeners/$', 'app1.listeners.views.show', name='show'),
	url(r'^listeners/show$', 'app1.listeners.views.show', name=''),
	url(r'^listeners/content$', 'app1.listeners.views.content'),

	# ログイン
	url(r'^login$', 'app1.views.login', name='login'),

	# ログアウト
	url(r'^logout$', 'app1.views.logout', name='logout'),

	# 謎の痕跡...
	url(r'^metro/$', 'app1.metro.views.default'),

	# top の表示
	url(r'^top/$', top_views_default.as_view(), name=''),
	url(r'^top/content$', top_views_content.as_view(), name=''),

	# レコード管理機能の痕跡
	url(r'^xusers/$', 'app1.xusers.views.show', name='show'),
	url(r'^xusers/show$', 'app1.xusers.views.show', name='show'),
	url(r'^xusers/add$', 'app1.xusers.views.add', name='add'),
	url(r'^xusers/add_complete$', 'app1.xusers.views.add_complete', name=''),

	# ファイル保管庫
	url(r'^images/$', 'app1.images.views.default'),
	url(r'^images/save$', 'app1.images.views.save'),
	url(r'^images/thumbnails$', 'app1.images.views.thumbnails'),
	# url(r'^images/$', images.as_view()),
)
