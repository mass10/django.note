# coding: utf-8

import os
import django
import logging
import subprocess
import time
import json
import project1
from app1.models import *

logger = logging.getLogger(__name__)

class util:

	@staticmethod
	def to_string(unknown):

		if unknown == None:
			return ''
#		return str(('' + unknown).encode('utf-8'))
		return django.utils.encoding.smart_unicode(unknown, encoding='utf-8')

	@staticmethod
	def validate_session(request):

		user_name = request.session.get('user')
		if user_name == None:
			logger.debug('session timed out. session_key=[' + util.to_string(request.session.session_key) + ']')
			return False
		# logger.debug(u'セッションは有効です。session_key=[' + util.to_string(request.session.session_key) + ']')
		logger.debug(u'セッションは有効です。')
		return True

	@staticmethod
	def enum_users():

		command_text = [os.path.join(project1.settings.BASE_DIR, 'bin/enum_users.py')]
		stream = subprocess.Popen(
			command_text,
			shell=False,
			stdout=subprocess.PIPE).stdout
		result = json.load(stream)
		stream.close()
		return result

	@staticmethod
	def iptables_list():

		command_text = [os.path.join(project1.settings.BASE_DIR, 'bin/enum_filters.py')]
		stream = subprocess.Popen(
			command_text,
			shell=False,
			stdout=subprocess.PIPE).stdout
		result = json.load(stream)
		stream.close()
		return result

	@staticmethod
	def listeners_list():

		command_text = [os.path.join(project1.settings.BASE_DIR, 'bin/enum_listeners.py')]
		stream = subprocess.Popen(
			command_text,
			shell=False,
			stdout=subprocess.PIPE).stdout
		result = json.load(stream)
		stream.close()
		return result

	@staticmethod
	def fill_menu_items(request, fields):

		if request.session.session_key == None:
			return
		# ユーザー名
		user_name = request.user.username
		# セッション有効時間
		elapsed = time.time() - request.session.get('logged_in_time')
		# 全ページで共通のフィールド
		fields_in_menu = {
			'session_key' : request.session.session_key,
			'user' : user_name,
			'logged_in_time' : int(elapsed)
		}
		fields['menuitems'] = fields_in_menu
