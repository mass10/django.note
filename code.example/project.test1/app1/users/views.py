# coding: utf-8

import django
import logging
import subprocess
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sessions.backends.cache import SessionStore
from app1.utils import *

logger = logging.getLogger(__name__)





def show(request):

	# =========================================================================
	# setup	
	# =========================================================================	
	fields = {}

	# =========================================================================
	# validation	
	# =========================================================================	
	if False == util.validate_session(request):
		logger.debug(u'ログインページへリダイレクトします。')
		return django.http.HttpResponseRedirect(u'/login')

	# =========================================================================
	# process
	# =========================================================================

	# ユーザーリストを抽出
	users = util.enum_users()

	# =========================================================================
	# contents
	# =========================================================================
	fields['form'] = {
		'users': users,
	}

	# メニュー処理
	util.fill_menu_items(request, fields)

	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('users/show.html')
	return django.http.HttpResponse(template.render(context))

def _fill_form_fields(request, fields):

	if fields.has_key('form_data') == False:
		fields['form_data'] = {}
	form_user = request.POST.get('users.add.form.user')
	form_password = request.POST.get('users.add.form.password')
	form_group = request.POST.get('users.add.form.group')
	fields['form_data']['user'] = util.to_string(form_user)
	fields['form_data']['password'] = util.to_string(form_password)
	fields['form_data']['group'] = util.to_string(form_group)

def _try_register_new_user(request, fields):

	###########################################################################
	# ユーザー登録処理
	#  ※TODO: model なりなんなりに移動すべき
	###########################################################################
	if request.method != 'POST':
		return False
	logger.debug(u'アカウントを作成します。')
	form_user = request.POST.get('users.add.form.user')
	form_password = request.POST.get('users.add.form.password')
	form_group = request.POST.get('users.add.form.group')
	logger.debug(u'form_user=[' + form_user + u']')
	logger.debug(u'form_password=[' + form_password + u']')
	logger.debug(u'form_group=[' + form_group + u']')
	command_text = [ 'sudo', '-u', 'root', 'useradd', form_user ]
	stream = subprocess.Popen(
		command_text,
		shell=False,
		stdout=subprocess.PIPE).stdout
	for line in stream:
		pass
	stream.close()
	return True

def add(request):

	# =========================================================================
	# setup	
	# =========================================================================	

	# =========================================================================
	# validation	
	# =========================================================================	
	if False == util.validate_session(request):
		logger.debug(u'ログインページへリダイレクトします。')
		return django.http.HttpResponseRedirect(u'/login')

	# =========================================================================
	# process
	# =========================================================================
	fields = {}

	#
	# ユーザーを登録
	#
	content_name = 'FORM_PAGE'
	if _try_register_new_user(request, fields):
		content_name = 'SUCCESS_PAGE'

	# =========================================================================
	# contents
	# =========================================================================
	if content_name == 'FORM_PAGE':

		#
		# この部分はメッセージを詰めてリダイレクトにすべきか
		#
		_fill_form_fields(request, fields)
		# メニュー処理
		util.fill_menu_items(request, fields)
		# コンテンツ返却
		context = django.template.RequestContext(request, fields)
		template = django.template.loader.get_template('users/add.html')
		return django.http.HttpResponse(template.render(context))

	logger.debug(u'完了ページへリダイレクトします。')
	return django.http.HttpResponseRedirect('/users/add_complete')

def add_complete(request):

	# =========================================================================
	# setup	
	# =========================================================================	

	# =========================================================================
	# validation	
	# =========================================================================	
	if False == util.validate_session(request):
		logger.debug(u'ログインページへリダイレクトします。')
		return django.http.HttpResponseRedirect(u'/login')

	# =========================================================================
	# process
	# =========================================================================
	fields = {}

	# =========================================================================
	# contents
	# =========================================================================

	# メニュー処理
	util.fill_menu_items(request, fields)
	# コンテンツ返却
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('users/add_complete.html')
	return django.http.HttpResponse(template.render(context))






