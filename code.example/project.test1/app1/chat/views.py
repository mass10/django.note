# coding: utf-8

import django
import logging
import subprocess
import hashlib
import inspect
import json
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from app1.utils import *
from app1.models import *
from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from app1.chat.form import *

logger = logging.getLogger(__name__)


@login_required
def default(request):

	# *************************************************************************
	# *************************************************************************
	# *************************************************************************
	#
	#
	# chat
	#
	#
	# *************************************************************************
	# *************************************************************************
	# *************************************************************************

	logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> $$$ start $$$');

	# =========================================================================
	# setup	
	# =========================================================================	
	fields = {}

	# =========================================================================
	# validation	
	# =========================================================================
	if request.method == 'POST':
		xform = MessageForm(request.POST)
		if xform.is_valid():
			print(u'投稿！');
			message_text = xform.cleaned_data.get('message_text', '')
			ChatMessageManager().create_new(request.user.username, message_text)
			return django.http.HttpResponseRedirect('/chat/')
		else:
			print(u'ミス！');

	# =========================================================================
	# process
	# =========================================================================

	# =========================================================================
	# contents
	# =========================================================================
	fields['window_title'] = 'lonely chat room!'
	fields['current_timestamp'] = datetime.datetime.now()
	fields['form'] = {
		'messages': ChatMessageManager().all()
	}
	# メニュー処理
	util.fill_menu_items(request, fields)
	# コンテンツ返却
	logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> --- end ---');
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('chat/default.html')
	return django.http.HttpResponse(template.render(context))

@login_required
def messages(request):

	fields = {}
	fields['form'] = {
		'messages': ChatMessageManager().all()
	}
	fields['current_timestamp'] = datetime.datetime.now()
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('chat/messages.html')
	return django.http.HttpResponse(template.render(context))
