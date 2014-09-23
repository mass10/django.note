# coding: utf-8

import django
import logging
import subprocess
import time
import inspect
from app1.utils import *
from app1.views import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

logger = logging.getLogger(__name__)

# class images(my_abstract_view):
#
	# template_name = 'images/default.html'

	# @method_decorator(login_required)
	# def get(self, request, *args, **kwargs):
	# 	return super(images, self).get(request, *args, **kwargs)

	# @method_decorator(login_required)
	# def save(self, request):
	# 	print 'save()'
	# 	return '<html>OK</html>'

@login_required
def default(request):

	# *************************************************************************
	# *************************************************************************
	# *************************************************************************
	#
	#
	# 保管庫のビュー
	#
	#
	# *************************************************************************
	# *************************************************************************
	# *************************************************************************

	# =========================================================================
	# setup	
	# =========================================================================	

	# =========================================================================
	# validation	
	# =========================================================================

	# =========================================================================
	# process
	# =========================================================================

	# =========================================================================
	# contents
	# =========================================================================
	fields = {}
	fields['window_title'] = u'保管庫'
	# メニュー処理
	util.fill_menu_items(request, fields)
	# コンテンツ返却
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('images/default.html')
	return django.http.HttpResponse(template.render(context))

def _save(f):

	return
	
	#
	# ファイルをデータベースに保管するように処理する
	#
	import uuid
	guid = uuid.uuid1()
	guid = str(guid)
	pathname = '/tmp/' + guid + ".tmp"
	stream = open(pathname, "wb")
	for bytes in f.chunks():
		size += stream.write(bytes)
	stream.close()
	return pathname

@login_required
def save(request):

	# *************************************************************************
	# *************************************************************************
	# *************************************************************************
	#
	#
	# 保管庫のビュー
	#
	#
	# *************************************************************************
	# *************************************************************************
	# *************************************************************************

	# =========================================================================
	# setup	
	# =========================================================================	

	# =========================================================================
	# validation	
	# =========================================================================
	if request.method == 'POST':
		pass
	else:
		return django.http.HttpResponseRedirect('/images/')

	# =========================================================================
	# process
	# =========================================================================

	# ファイルの保存
	for e in request.FILES:
		_save(e)

	# =========================================================================
	# contents
	# =========================================================================
	fields = {}
	fields['window_title'] = u'保管庫'
	# メニュー処理
	util.fill_menu_items(request, fields)
	# コンテンツ返却
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('images/default.html')
	return django.http.HttpResponse(template.render(context))
