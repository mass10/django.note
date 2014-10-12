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
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import ugettext
from app1.utils import *
from app1.form import *
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

# Create your views here.

logger = logging.getLogger(__name__)

# out = codecs.getwriter('utf-8')(sys.stdout)

@login_required
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

@login_required
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
	password = login_form.cleaned_data.get('password')
	if user_name == None or user_name == '':
		logger.info(u'ユーザー [' + util.to_string(user_name) + u'] によるログイン失敗。理由=[ユーザーID入力なし], session_key=[' + util.to_string(request.session.session_key) + ']')
		return False
	# if user_name.find('@') == -1:
	# 	logger.debug(u'ユーザー [' + util.to_string(user_name) + u'] によるログイン失敗。session_key=[' + util.to_string(request.session.session_key) + ']')
	# 	return False

	# user_name = 'unknown@example.com'

	# =========================================================================
	# ログイン処理
	# =========================================================================

	# 通常のログイン
	# user = django.contrib.auth.authenticate(username=user_name, password=password)

	# メールアドレスでログインする方法を検証中...
	user = django.contrib.auth.authenticate(email=user_name, password=password)

	if user is None:
		logger.info(u'ユーザー [' + util.to_string(user_name) + u'] によるログイン失敗。理由=[アカウント情報不正]')
		return False
	elif not user.is_active:
		logger.info(u'ユーザー [' + util.to_string(user_name) + u'] によるログイン失敗。理由=[アカウントは inactive です]')
		return False
	else:
		logger.info(u'ユーザー [' + util.to_string(user_name) + u'] によるログイン成功！')
		django.contrib.auth.login(request, user)
		pass

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
	# request.session.save()

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
	fields = {}
	if request.method == 'POST':
		fields['error_message'] = u'ログイン画面のテストです。MAIL ADDRESS にメールアドレスを入力してください。'
	login_form = LoginForm(request.POST)
	login_form.is_valid()
	fields['form_data'] = login_form
	fields['greeting_message_text'] = ugettext('Welcome to my site.')
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('login.html')
	logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> --- end ---');
	return django.http.HttpResponse(template.render(context))

def _logout(request):

	logger.debug(u'ユーザー [' + util.to_string(request.session.get('user')) + u'] がログアウトしました。')
	django.contrib.auth.logout(request)

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

class my_abstract_view(TemplateView):

	template_name = 'must be overridden'

	def dispatch(self, request, *args, **kwargs):
		print(my_abstract_view.dispatch)
		return super(my_abstract_view, self).dispatch(request, *args, **kwargs)

	def get(self, request, *args, **kwargs):
		print(my_abstract_view.get)
		return super(my_abstract_view, self).get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		print(my_abstract_view.get)
		return super(my_abstract_view, self).post(request, *args, **kwargs)
