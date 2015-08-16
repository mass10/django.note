# coding: utf-8

import sys
import django
import logging
import inspect
import project1
from app1.utils import *
from app1.form import *
from django.contrib.auth.decorators import login_required

# Create your views here.

logger = logging.getLogger(__name__)

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
	fields['window_title'] = 'metro'
	util.fill_menu_items(request, fields)
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('metro/default.html')
	return django.http.HttpResponse(template.render(context))
