# coding: utf-8

import django
import logging

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
			