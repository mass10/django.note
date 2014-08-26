# coding: utf-8

import sys
import codecs
import django
import uuid
import json
import logging
import subprocess
import datetime
import time
import inspect
import project1
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sessions.backends.cache import SessionStore
from app1.utils import *
from app1.form import *

# Create your views here.

logger = logging.getLogger(__name__)

# out = codecs.getwriter('utf-8')(sys.stdout)

def api(request):

	# *************************************************************************
	# *************************************************************************
	# *************************************************************************
	#
	#
	# 単純な文字列を返却するアクションの例
	#
	#
	# *************************************************************************
	# *************************************************************************
	# *************************************************************************

	logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> $$$ start $$$');

	# =========================================================================
	# setup	
	# =========================================================================	
	current_user = request.session.get('user', '')

	# =========================================================================
	# validation	
	# =========================================================================	

	# =========================================================================
	# process
	# =========================================================================

	# =========================================================================
	# contents
	# =========================================================================
	response = {
		'response': 'hello',
		'current_user': current_user,
	}
	logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> --- end ---');
	return django.http.HttpResponse(json.dumps(response))

def default(request):

	# *************************************************************************
	# *************************************************************************
	# *************************************************************************
	#
	#
	# デフォルトページのアクション
	#
	#
	# *************************************************************************
	# *************************************************************************
	# *************************************************************************

	logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> $$$ start $$$');
	logger.info('COOKIES=[' + str(request.COOKIES) + ']');
	logger.info('BASE_DIR=[' + project1.settings.BASE_DIR + ']');

	# =========================================================================
	# setup	
	# =========================================================================	
	user_name = request.session.get('user')

	# =========================================================================
	# validation	
	# =========================================================================	
	if False == util.validate_session(request):
		logger.debug(u'ログインページへリダイレクトします。')
		logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> --- end ---');
		return django.http.HttpResponseRedirect('/login')

	# =========================================================================
	# process
	# =========================================================================
	
	# =========================================================================
	# contents
	# =========================================================================
	logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> --- end ---');
	fields = {}
	fields['window_title'] = 'HOME'
	util.fill_menu_items(request, fields)
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('index.html')
	return django.http.HttpResponse(template.render(context))

def _try_login(request):

	if request.method != 'POST':
		return False

	logger.debug(u'ログインリクエストを検出しました。')

	# =========================================================================
	# フォーム検証
	# =========================================================================
	login_form = LoginForm(request.POST)
	if not login_form.is_valid():
		pass
	user_name = login_form.cleaned_data.get('user_id')
	if user_name == None or user_name == '':
		logger.debug(u'ユーザー [' + util.to_string(user_name) + u'] によるログイン失敗。session_key=[' + util.to_string(request.session.session_key) + ']')
		return False
	if user_name.find('@') == -1:
		logger.debug(u'ユーザー [' + util.to_string(user_name) + u'] によるログイン失敗。session_key=[' + util.to_string(request.session.session_key) + ']')
		return False

	# =========================================================================
	# ログイン処理
	# =========================================================================

	# ログインユーザー
	request.session['user'] = util.to_string(user_name)
	# ログイン日時
	request.session['logged_in_time'] = time.time()
	# 長い文字列
	request.session['long_item'] = [
		u'ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ',
		u'ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ',
		u'ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ',
		u'ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ',
		u'ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ',
		u'ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ',
		u'ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ',
		u'ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ',
		u'ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ',
	]
	# セッション有効期間
	#   - 0:ウェブブラウザを閉じるまで
	request.session.set_expiry(0)
	# save() によって session_key が発行される
	request.session.save()

	logger.debug(u'ユーザー [' + util.to_string(user_name) + u'] がログインしました。新しいセッションが開始されました。')

	return True

def login(request):

	# *************************************************************************
	# *************************************************************************
	# *************************************************************************
	#
	#
	# ログインページ的なもの
	#
	#
	# *************************************************************************
	# *************************************************************************
	# *************************************************************************
	logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> $$$ start $$$');
	
	# =========================================================================
	# setup	
	# =========================================================================

	# =========================================================================
	# validation	
	# =========================================================================	
	if _try_login(request):
		logger.debug(u'トップページへリダイレクトします。')
		logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> --- end ---');
		return django.http.HttpResponseRedirect('/')

	# =========================================================================
	# process
	# =========================================================================

	# =========================================================================
	# contents
	# =========================================================================
	logger.debug(u'コンテンツ出力')
	fields = {}
	login_form = LoginForm(request.POST)
	if request.method == 'POST':
		fields['error_message'] = u'ログイン画面のテストです。MAIL ADDRESS にメールアドレスを入力してください。'
	fields['form_data'] = login_form
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('login.html')
	logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> --- end ---');
	return django.http.HttpResponse(template.render(context))

def _logout(request):

	logger.debug(u'ユーザー [' + util.to_string(request.session.get('user')) + u'] がログアウトしました。')
	request.session.clear()

def logout(request):

	# *************************************************************************
	# *************************************************************************
	# *************************************************************************
	#
	#
	# ログアウトのアクション
	#
	#
	# *************************************************************************
	# *************************************************************************
	# *************************************************************************
	logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> $$$ start $$$');
	
	# =========================================================================
	# setup	
	# =========================================================================	

	# =========================================================================
	# validation	
	# =========================================================================	

	# =========================================================================
	# process
	# =========================================================================
	_logout(request)

	# =========================================================================
	# contents
	# =========================================================================
	logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> --- end ---');
	return django.http.HttpResponseRedirect('/')
