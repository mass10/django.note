# coding: utf-8

import django
import logging
import subprocess
import hashlib
import inspect
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sessions.backends.cache import SessionStore
from app1.utils import *
from app1.xusers.form import *
from app1.models import *
from django.shortcuts import *
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)


@login_required
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

	logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> $$$ start $$$');

	# =========================================================================
	# setup	
	# =========================================================================	
	fields = {}

	# =========================================================================
	# validation	
	# =========================================================================	

	# =========================================================================
	# process
	# =========================================================================

	# ユーザーリストを抽出
	# users = util.enum_users()
	users = PersonManager().list_all()

	# =========================================================================
	# contents
	# =========================================================================
	fields['form'] = {
		'users': users,
	}
	fields['window_title'] = 'ユーザー一覧'
	# メニュー処理
	util.fill_menu_items(request, fields)
	# コンテンツ返却
	logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> --- end ---');
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('xusers/show.html')
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

	form_user_id = user_form.cleaned_data.get('user_id')
	form_password = user_form.cleaned_data.get('password')
	form_first_name = user_form.cleaned_data.get('first_name')
	form_last_name = user_form.cleaned_data.get('last_name')
	form_mail = user_form.cleaned_data.get('mail')

	# =========================================================================
	# ユーザーを登録します。
	# =========================================================================
	logger.debug(u'新しいアカウントを作成します。')

	new_entry = Person.objects.create(
		user_id=form_user_id,
		first_name=form_first_name,
		last_name=form_last_name,
		mail=form_mail,
		password=form_password)
	generator = hashlib.sha256()
	new_entry.password = generator.update(new_entry.password)
	new_entry.save()

	logger.debug(u'新しいアカウントを作成しました。')
	return True

@login_required
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

	# =========================================================================
	# process
	# =========================================================================

	fields = {}
	
	# ユーザーを登録
	if _try_to_register_new_user(request, fields):
		logger.debug(u'完了ページへリダイレクトします。')
		return django.http.HttpResponseRedirect('/xusers/add_complete')

	# =========================================================================
	# contents
	# =========================================================================
	# メニュー処理
	util.fill_menu_items(request, fields)
	# このコンテンツのポスト先
	fields['page_action'] = '/xusers/add'
	# ウィンドウのタイトル
	fields['window_title'] = 'ユーザー登録'
	# コンテンツ返却
	fields['form_data'] = UserForm(request.POST)
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('xusers/add.html')
	return django.http.HttpResponse(template.render(context))

@login_required
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
	template = django.template.loader.get_template('xusers/add_complete.html')
	return django.http.HttpResponse(template.render(context))
