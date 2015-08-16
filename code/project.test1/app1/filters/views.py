# coding: utf-8

import django
import uuid
import json
import logging
import subprocess
import inspect
from django.shortcuts import render
from app1.utils import *
from django.contrib.auth.decorators import login_required

# Create your views here.

logger = logging.getLogger(__name__)

@login_required
def show(request):

	###########################################################################
	# netfilter の状態を表示するビュー
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
	logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> --- end ---');
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('filters/show.html')
	return django.http.HttpResponse(template.render(context))

def content(request):

	###########################################################################
	# netfilter の状態を表示するビュー
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
	template = django.template.loader.get_template('filters/content.html')
	return django.http.HttpResponse(template.render(context))
