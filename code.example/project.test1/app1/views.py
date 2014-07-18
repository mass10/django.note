# :encoding: utf-8

import django
import uuid
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sessions.backends.cache import SessionStore

# Create your views here.




def api(request):

	#
	# 単純な文字列を返却するアクションの例
	#

	response = {
		'response': 'hello',
		'current_user': request.session.get('user', ''),
	}
	return django.http.HttpResponse(json.dumps(response))

def main(request):

	# session_id = get_session_id(request)
	user_name = request.session.get('user')
	fields = {
		'session': {
			'session_key' : request.session.session_key,
			'user' : user_name,
		}
	}
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('index.html')
	return django.http.HttpResponse(template.render(context))

def get_session_id(request):
	
	session_id = request.session.session_key
	if session_id == None:
		request.session.save()
		session_id = request.session.session_key
	return session_id

def try_login(request):

	user_name = request.POST['login.user']
	if len(user_name) == 0:
		return False
	request.session['user'] = user_name
	return True

def login(request):

	#
	# ログインページ的なもの
	#
	if request.method == 'POST':
		if try_login(request):
			return django.http.HttpResponseRedirect('/')
	fields = {}
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('login.html')
	return django.http.HttpResponse(template.render(context))














def hello(request):

	#
	# テンプレートを利用したアクションの例
	#

	fields = {}
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('hello.html')
	return django.http.HttpResponse(template.render(context))










