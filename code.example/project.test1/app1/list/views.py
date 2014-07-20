# coding: utf-8

import django
import uuid
import json
import logging
import subprocess
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sessions.backends.cache import SessionStore

# Create your views here.

logger = logging.getLogger(__name__)


def show(request):

	logger.info('<' + __name__ + '> $$$ start $$$');

	filters = _iptables_list(request)

	user_name = request.session.get('user')

	fields = {
		'session': {
			'session_key' : request.session.session_key,
			'user' : user_name,
		},
		'form': {
			'filters': filters,
		},
	}
	context = django.template.RequestContext(
		request, fields)
	template = django.template.loader.get_template(
		'list/show.html')
	return django.http.HttpResponse(
		template.render(context))

def _analyze_filter_line(line):
	if line == '':
		return None
	fields = line.split()
	if fields[0] == 'num':
		return None
	if fields[0] == 'Chain':
		return None
	return fields

def _create_node(tree, name):
	if tree.has_key(name):
		return
	tree[name] = []

def _iptables_list(request):

	command_text = ['sudo', '-u', 'root', '/sbin/iptables', '--list', '-nvx', '--line-numbers']

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
				_create_node(result, current_section)
			elif fields[1] == 'FORWARD':
				current_section = 'FORWARD'
				_create_node(result, current_section)
			elif fields[1] == 'OUTPUT':
				current_section = 'OUTPUT'
				_create_node(result, current_section)
			else:
				pass
		else:
			if current_section == None:
				continue
			result[current_section].append(line)

	stream.close()

	return result
