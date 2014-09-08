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
	fields['page_action'] = '/events/'
	fields['window_title'] = 'HTML events'
	util.fill_menu_items(request, fields)
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('events/default.html')
	return django.http.HttpResponse(template.render(context))

