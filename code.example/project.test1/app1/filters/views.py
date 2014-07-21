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

def show(request):

	# *************************************************************************
	# *************************************************************************
	# *************************************************************************
	#
	#
	# netfilter の状態を表示するアクション
	#
	#
	# *************************************************************************
	# *************************************************************************
	# *************************************************************************

	logger.info('<' + __name__ + '> $$$ start $$$');

	# =========================================================================
	# setup	
	# =========================================================================	

	# =========================================================================
	# validation	
	# =========================================================================	
	if False == util.validate_session(request):
		logger.debug('トップページへリダイレクトします。')
		return django.http.HttpResponseRedirect('/')

	# =========================================================================
	# process
	# =========================================================================

	# current user
	user_name = request.session.get('user')
	# netfilter の設定をロード
	filters = util.iptables_list()

	# =========================================================================
	# contents
	# =========================================================================
	fields = {}
	fields['form'] = {
		'filters': filters,
	}
	util.fill_menu_items(request, fields)
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('filters/show.html')
	logger.debug('コンテンツを返します。')
	return django.http.HttpResponse(template.render(context))

