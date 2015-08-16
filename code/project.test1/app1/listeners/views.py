# coding: utf-8

import django
import logging
import subprocess
import time
import inspect
import datetime
from app1.utils import *
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)

@login_required
def show(request):

	###########################################################################
	# netstat の状態を表示するビュー
	###########################################################################

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

	# =========================================================================
	# contents
	# =========================================================================
	fields = {}
	util.fill_menu_items(request, fields)
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('listeners/show.html')
	logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> --- end ---');
	return django.http.HttpResponse(template.render(context))

@login_required
def content(request):

	###########################################################################
	# netstat の状態を表示するビュー
	###########################################################################

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

	# netstat の設定をロード
	listeners = util.listeners_list()

	# =========================================================================
	# contents
	# =========================================================================
	fields = {}
	fields['c'] = {
		'listeners': listeners,
		'current_timestamp': datetime.datetime.now(),
	}
	util.fill_menu_items(request, fields)
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('listeners/content.html')
	logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> --- end ---');
	return django.http.HttpResponse(template.render(context))
