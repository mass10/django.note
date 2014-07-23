# coding: utf-8

import django
import logging
import subprocess
import time

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
		logger.debug(u'セッションは有効です。session_key=[' + util.to_string(request.session.session_key) + ']')
		return True

	@staticmethod
	def iptables_list():

		#
		# この部分は外部コマンドに委譲すべき。
		#

		command_text = [
			'sudo',
			'-u',
			'root',
			'/sbin/iptables',
			'--list',
			'-nvx',
			'--line-numbers']

		stream = subprocess.Popen(
			command_text,
			shell=False,
			stdout=subprocess.PIPE).stdout

		result = {}

		current_section = None

		for line in stream:

			line = line.strip()
			if line == '':
				continue

			fields = line.split()
			if fields[0] == 'num':
				continue
			elif fields[0] == 'Chain':
				if fields[1] == 'INPUT':
					current_section = 'INPUT'
					util._create_node(result, current_section)
				elif fields[1] == 'FORWARD':
					current_section = 'FORWARD'
					util._create_node(result, current_section)
				elif fields[1] == 'OUTPUT':
					current_section = 'OUTPUT'
					util._create_node(result, current_section)
				else:
					pass
			else:
				if current_section == None:
					continue
				result[current_section].append(line)

		stream.close()

		#
		# 戻りは正しいデータクラスを提供する。生の配列やリストをみだりに使わない。
		#

		return result

	@staticmethod
	def listeners_list():

		#
		# この部分は外部コマンドに委譲すべき。
		#

		command_text = ['sudo', '-u', 'root', '/bin/netstat', '-ntlp']

		stream = subprocess.Popen(
			command_text,
			shell=False,
			stdout=subprocess.PIPE).stdout

		result = []

		current_section = None

		for line in stream:

			line = line.strip()

			if line == '':
				continue

			result.append(line)

		stream.close()

		#
		# 戻りは正しいデータクラスを提供する。生の配列やリストをみだりに使わない。
		#

		return result

	@staticmethod
	def _create_node(tree, name):

		if tree.has_key(name):
			return

		tree[name] = []

	@staticmethod
	def fill_menu_items(request, fields):

		if request.session.session_key == None:
			return
		# ユーザー名
		user_name = request.session.get('user')
		# セッション有効時間
		elapsed = time.time() - request.session.get('logged_in_time')
		# 全ページで共通のフィールド
		fields_in_menu = {
			'session_key' : request.session.session_key,
			'user' : user_name,
			'logged_in_time' : int(elapsed)
		}
		fields['menuitems'] = fields_in_menu
