# coding: utf-8

import django
import logging
import subprocess
import time
import inspect
from app1.utils import *
from django.contrib.auth.decorators import login_required
from app1.models import *

logger = logging.getLogger(__name__)

@login_required
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

	logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> $$$ start $$$');

	# =========================================================================
	# setup	
	# =========================================================================	

	# =========================================================================
	# validation	
	# =========================================================================	
	# if False == util.validate_session(request):
	# 	logger.debug(u'トップページへリダイレクトします。')
	# 	logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> --- end ---');
	# 	return django.http.HttpResponseRedirect('/')

	# =========================================================================
	# process
	# =========================================================================
	result = Top().get()

	# =========================================================================
	# contents
	# =========================================================================
	fields = {}
	fields['form'] = {
		'lines': result,
	}
	util.fill_menu_items(request, fields)
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('top/show.html')
	logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> --- end ---');
	return django.http.HttpResponse(template.render(context))
