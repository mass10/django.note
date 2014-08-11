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
	user_name = request.session.get(u'user')
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
	util.fill_menu_items(request, fields)
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('users/show.html')
	return django.http.HttpResponse(template.render(context))
