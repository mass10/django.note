# coding: utf-8

import django
import uuid
import json
import logging
import subprocess
import inspect
from django.shortcuts import render
from django.http import HttpResponse
from app1.utils import *
from django.contrib.auth.decorators import login_required

# Create your views here.

logger = logging.getLogger(__name__)

@login_required
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

	logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> $$$ start $$$');

	# =========================================================================
	# setup	
	# =========================================================================	

	# =========================================================================
	# validation	
	# =========================================================================	
	# if False == util.validate_session(request):
	# 	logger.debug('トップページへリダイレクトします。')
	# 	logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> --- end ---');
	# 	return django.http.HttpResponseRedirect('/')

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
	logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> --- end ---');
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('filters/show.html')
	return django.http.HttpResponse(template.render(context))

