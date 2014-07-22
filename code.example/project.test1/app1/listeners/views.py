# coding: utf-8

import django
import logging
import subprocess
import time
from app1.utils import *

logger = logging.getLogger(__name__)

def show(request):

	# *************************************************************************
	# *************************************************************************
	# *************************************************************************
	#
	#
	# netstat の状態を表示するアクション
	#
	#
	# *************************************************************************
	# *************************************************************************
	# *************************************************************************

	logger.info('$$$ start $$$');

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
	# netstat の設定をロード
	listeners = util.listeners_list()

	# =========================================================================
	# contents
	# =========================================================================
	fields = {}
	fields['form'] = {
		'listeners': listeners,
	}
	util.fill_menu_items(request, fields)
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('listeners/show.html')
	logger.debug('コンテンツを返します。')
	return django.http.HttpResponse(template.render(context))

