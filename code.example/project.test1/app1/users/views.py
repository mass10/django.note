# coding: utf-8

import django
import logging
import subprocess
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sessions.backends.cache import SessionStore
from app1.utils import *
from app1.users.form import *
from app1.models import *

logger = logging.getLogger(__name__)



def show(request):

	# *************************************************************************
	# *************************************************************************
	# *************************************************************************
	#
	#
	# ユーザー一覧
	#
	#
	# *************************************************************************
	# *************************************************************************
	# *************************************************************************

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
	logger.debug(u'コンテンツを返します。')
	fields['form'] = {
		'users': users,
	}
	fields['window_title'] = 'ユーザー一覧'
	# メニュー処理
	util.fill_menu_items(request, fields)
	# コンテンツ返却
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('users/show.html')
	return django.http.HttpResponse(template.render(context))

def _try_to_register_new_user(request, fields):

	#
	# ユーザー登録処理
	#  ※TODO: model なりなんなりに移動すべき
	#
	if request.method != 'POST':
		return False

	# =========================================================================
	# フォーム検証
	# =========================================================================
	user_form = UserForm(request.POST)
	if not user_form.is_valid():
		fields['form_data'] = user_form
		logger.debug(str(user_form))
		logger.debug(u'入力エラーにより要求は拒否されました。')
		return False

	# =========================================================================
	# フォームに入力された内容を取り出しています。
	# =========================================================================
	form_user = user_form.cleaned_data.get('user_id')
	form_password = user_form.cleaned_data.get('password')
	form_group = user_form.cleaned_data.get('group_id')

	logger.debug(u'user_id=[' + util.to_string(form_user) + ']')
	logger.debug(u'password=[' + util.to_string(form_password) + ']')
	logger.debug(u'group_id=[' + util.to_string(form_group) + ']')

	fields['form_data'] = user_form

	# =========================================================================
	# ユーザーを登録します。
	# =========================================================================
	logger.debug(u'新しいアカウントを作成します。')

	# モデルを用いて新しいレコードを作成する方法
	if 0:
		new_entry = Person.objects.create(first_name='Akjwiueh Kajiiqkx')
		new_entry.save()

	if 0:
		command_text = [ 'sudo', '-u', 'root', 'useradd', form_user ]
		stream = subprocess.Popen(
			command_text,
			shell=False,
			stdout=subprocess.PIPE).stdout
		for line in stream:
			pass
		stream.close()

	logger.debug(u'新しいアカウントを作成しました。')

	return True

def add(request):

	# *************************************************************************
	# *************************************************************************
	# *************************************************************************
	#
	#
	# ユーザー登録フォーム
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
	if False == util.validate_session(request):
		logger.debug(u'ログインページへリダイレクトします。')
		return django.http.HttpResponseRedirect(u'/login')

	# =========================================================================
	# process
	# =========================================================================

	fields = {}
	
	# ユーザーを登録
	if _try_to_register_new_user(request, fields):
		logger.debug(u'完了ページへリダイレクトします。')
		return django.http.HttpResponseRedirect('/users/add_complete')

	# =========================================================================
	# contents
	# =========================================================================
	# メニュー処理
	util.fill_menu_items(request, fields)
	# このコンテンツのポスト先
	fields['page_action'] = '/users/add'
	# ウィンドウのタイトル
	fields['window_title'] = 'ユーザー登録'
	# コンテンツ返却
	fields['form_data'] = UserForm(request.POST)
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('users/add.html')
	return django.http.HttpResponse(template.render(context))

def add_complete(request):

	# *************************************************************************
	# *************************************************************************
	# *************************************************************************
	#
	#
	# ユーザー登録完了ページ
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
	# ウィンドウのタイトル
	fields['window_title'] = 'ユーザー登録完了'
	# メニュー処理
	util.fill_menu_items(request, fields)
	# コンテンツ返却
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('users/add_complete.html')
	return django.http.HttpResponse(template.render(context))
