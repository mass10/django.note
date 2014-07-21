# coding: utf-8

import django
import uuid
import json
import logging
import subprocess
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

	logger.info('<app1.views.api> $$$ start $$$');

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

	logger.info('<app1.views.main> $$$ start $$$');

	# =========================================================================
	# setup	
	# =========================================================================	
	user_name = request.session.get('user')

	# =========================================================================
	# validation	
	# =========================================================================	
	if not util.validate_session(request):
		return django.http.HttpResponseRedirect('/login')

	# =========================================================================
	# process
	# =========================================================================
	
	# =========================================================================
	# contents
	# =========================================================================
	fields = {
		'session': {
			'session_key' : request.session.session_key,
			'user' : user_name,
		}
	}
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('index.html')
	return django.http.HttpResponse(template.render(context))

def _try_login(request):

	if request.method != 'POST':
		return False
	user_name = request.POST.get('login.user')
	if len(user_name) == 0:
		return False
	request.session['user'] = user_name
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
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('login.html')
	return django.http.HttpResponse(template.render(context))
