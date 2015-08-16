# coding: utf-8

import datetime

class stopwatch:

	_value = None

	def __init__(self):
		self._member = datetime.datetime.now()

	def __repr__(self):
		current = datetime.datetime.now()
		elapsed = current - self._member
		return str(elapsed)
