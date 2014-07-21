# coding: utf-8

import django
import logging
import subprocess

logger = logging.getLogger(__name__)

class util:

	@staticmethod
	def to_string(unknown):

		if unknown == None:
			return ''
		return str(unknown)

	@staticmethod
	def validate_session(request):

		user_name = request.session.get('user')
		if user_name == None:
			logger.debug('セッションが切れている')
			return False
		return True

	@staticmethod
	def iptables_list(request):

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

		return result

	@staticmethod
	def _create_node(tree, name):

		if tree.has_key(name):
			return

		tree[name] = []

