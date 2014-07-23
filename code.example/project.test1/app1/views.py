# coding: utf-8

import django
import uuid
import json
import logging
import subprocess
import datetime
import time
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sessions.backends.cache import SessionStore
from app1.utils import *

# Create your views here.

logger = logging.getLogger(__name__)


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

	logger.info('<api> $$$ start $$$');

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
	logger.info('<app1.views.api> --- end ---');
	return django.http.HttpResponse(json.dumps(response))

def main(request):

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

	logger.info('<main> $$$ start $$$');
	logger.info('<main> ' + str(request.COOKIES));

	# =========================================================================
	# setup	
	# =========================================================================	
	user_name = request.session.get('user')

	# =========================================================================
	# validation	
	# =========================================================================	
	if False == util.validate_session(request):
		logger.debug(u'ログインページへリダイレクトします。')
		return django.http.HttpResponseRedirect('/login')

	# =========================================================================
	# process
	# =========================================================================
	
	# =========================================================================
	# contents
	# =========================================================================
	fields = {}
	util.fill_menu_items(request, fields)
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('index.html')
	return django.http.HttpResponse(template.render(context))

def _try_login(request):

#	if request.method != 'POST':
#		return False

	user_name = request.REQUEST.get('login_form.user')
	if user_name == None or user_name == '':
		logger.debug(u'ユーザー [' + util.to_string(user_name) + u'] によるログイン失敗。session_key=[' + util.to_string(request.session.session_key) + ']')
		return False

	# ログインユーザー
	request.session['user'] = util.to_string(user_name)
	# ログイン日時
	request.session['logged_in_time'] = time.time()
	# 長い文字列
	request.session['long_item'] = [
		u'ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ',
		'ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ',
		'ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ',
		'ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ',
		'ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ',
		'ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ',
		'ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ',
		'ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ',
		'ああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ',
	]
	# セッション有効期間
	#   - 0:ウェブブラウザを閉じるまで
	request.session.set_expiry(0)
	# save() によって session_key が発行される
	request.session.save()

	logger.debug(u'ユーザー [' + util.to_string(user_name) + u'] がログインしました。新しいセッションが開始されました。session_key=[' + str(request.session.session_key) + ']')

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
	logger.debug('<login> $$$ start $$$')
	
	# =========================================================================
	# setup	
	# =========================================================================

	# =========================================================================
	# validation	
	# =========================================================================	
	if _try_login(request):
		return django.http.HttpResponseRedirect('/')

	# =========================================================================
	# process
	# =========================================================================

	# =========================================================================
	# contents
	# =========================================================================
	fields = {}
	
	if request.method == 'POST':
		fields['login_form'] = {
			'error_message': u'ログイン画面のテストです。MAIL ADDRESS に何か文字列を入力してください。',
		}
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('login.html')
	return django.http.HttpResponse(template.render(context))

def _logout(request):

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
	logger.debug('<logout> $$$ start $$$')
	
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
	return django.http.HttpResponseRedirect('/')
