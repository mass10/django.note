# coding: utf-8

import django
import urllib
import uuid
import json
import logging
import requests
import pymongo
from django.shortcuts import render

# Create your views here.

logger = logging.getLogger(__name__)

application_token = uuid.uuid1()




def _env():

	file = open('/root/googleapi-test-keys.json')
	j = json.load(file)
	file.close()
	return j



def _update_user(user_id, id_token):

	if user_id == None or user_id == '':
		print 'パラメータのエラーです (user_id is "")'
		raise ''

	if id_token == None or id_token == '':
		print 'パラメータのエラーです (id_token is "")'
		raise ''


	# =========================================================================
	# 保存すべきはどれか？？
	# - access_token
	# - id_token
	# - (Google が返してきた)user_id
	#                           などいろいろある
	# =========================================================================



	client = pymongo.MongoClient('localhost', 27017, )
	db = client['glogin_sample_app_db']
	known_users = db['known_users']

	# update(1つだけ抽出する方法は？)
	for e in known_users.find({'user_id': user_id}):
		e['id_token'] = id_token
		print('ユーザー [{0}] と id_token [{1}] が保存されました。').format(user_id, id_token)
		return None

	# or insert
	known_users.insert_one({'user_id': user_id, 'id_token': id_token})
	print('ユーザー [{0}] と id_token [{1}] が保存されました。').format(user_id, id_token)
	return None

#
# ユーザーをデータベースから探します。
#
def _find_user(user_id):

	if user_id == None:
		return ''
	if user_id == '':
		return ''

	print '[debug] MongoDB からユーザーを検索しています... [{0}]'.format(user_id)

	client = pymongo.MongoClient('localhost', 27017, )
	db = client['glogin_sample_app_db']
	known_users = db['known_users']

	id_token = ''
	for e in known_users.find({'user_id': user_id}):
		id_token = e.get('id_token')
	if id_token == '':
		print '不明なログインです'
		return None

	print 'ユーザーがみつかりました。メールアドレスを照会します。'

	return _try_to_get_email(id_token)

#
# [XXさん] テキストの生成
#
def _create_identity_text(email):

	identity_text = ''
	if email != None and 0 < len(email):
		identity_text = 'ようこそ {0} さん'.format(email)
	else:
		identity_text = 'ようこそ ななし さん'
	return identity_text

def index(request):

	if request.method == 'POST':
		return _redirect_to_google(request)

	user_id = request.COOKIES.get('user_id')
	print '### REQUEST ###'
	print '[user_id]=[{0}] (from COOKIE)'.format(user_id)

	# =========================================================================
	# 現在のユーザーを調べる
	# =========================================================================
	current_user_email = _find_user(user_id)
	if current_user_email == '':
		user_id = uuid.uuid1()

	# =========================================================================
	# コンテンツ生成
	# =========================================================================
	identity_text = _create_identity_text(current_user_email)
	fields = {}
	fields['identity_text'] = identity_text
	context = django.template.RequestContext(request, fields)
	template = django.template.loader.get_template('index.html')
	response = django.http.HttpResponse(template.render(context))
	response.set_cookie('user_id', user_id)
	return response

def _redirect_to_google(request):

	env = _env()

	client_id = env['client_id']
	
	guid = uuid.uuid1()
	guid = str(guid)

	redirect_uri = 'http://www.example.com/glogin'

	scope = 'email profile'

	google_url = 'https://accounts.google.com/o/oauth2/auth' + '?client_id=' + urllib.quote_plus(client_id) + '&response_type=code' + '&scope=' + urllib.quote_plus(scope) + '&redirect_uri=' + urllib.quote_plus(redirect_uri) + '&state=' + urllib.quote_plus(guid) + '&device_id='

	# logger.info(google_url)
	
	return django.http.HttpResponseRedirect(google_url)

def glogin(request):

	# =========================================================================
	# initialization
	# =========================================================================
	state = request.GET.get('state')
	code = request.GET.get('code')
	user_id = request.COOKIES.get('user_id')

	print '[debug] state={0}, code={1}'.format(state, code)

	env = _env()
	client_id = env['client_id']
	client_secret = env['client_secret']

	# =========================================================================
	# validation
	# =========================================================================


	# =========================================================================
	# processing
	# =========================================================================
	fields = {}
	fields['code'] = code
	fields['client_id'] = client_id
	fields['client_secret'] = client_secret
	fields['redirect_uri'] = 'http://www.example.com/glogin'
	fields['grant_type'] = 'authorization_code'

	response = requests.post('https://www.googleapis.com/oauth2/v3/token', params = fields)

	print '[DEBUG] RESPONSE: %s' % response.text

	try:

		print '[DEBUG] reading response...'

		j = json.loads(response.text)
		if not j.has_key('access_token'):
			print '[debug] \'access_token\' not found.'
			return django.http.HttpResponseRedirect('/')
		if not j.has_key('id_token'):
			return django.http.HttpResponseRedirect('/')

		access_token = j.get('access_token')
		expires_in = j.get('expires_in')
		id_token = j.get('id_token')

		email = _try_to_get_email(id_token)
		if email == None or email == '':
			# メールアドレスの照会に失敗しています。
			return django.http.HttpResponseRedirect('/')

		# token とユーザーを紐づけてデータベースに保管します。
		_update_user(user_id, id_token)

	except:

		raise ''

	# =========================================================================
	# finalization
	# =========================================================================

	return django.http.HttpResponseRedirect('/')

def _try_to_get_email(id_token):

	# =========================================================================
	# キーなどを読出し
	# =========================================================================
	env = _env()

	client_id = env['client_id']

	print '[debug] ユーザー情報を照会中... client_id=[{0}], id_token=[{1}]'.format(client_id, id_token)

	if id_token == None or id_token == '':
		print '[debug] パラメータのエラーです。'
		return None





	# =========================================================================
	# Google アカウント情報を問い合わせています。
	# =========================================================================

	email = None

	# Google にアカウント情報を問い合わせています。
	response = requests.get('https://www.googleapis.com/oauth2/v1/tokeninfo?id_token=' + urllib.quote_plus(id_token))

	print '[DEBUG] RESPONSE(=ユーザーの情報): {0}'.format(response.text)

	# =========================================================================
	# レスポンスの読出し
	# =========================================================================

	j = json.loads(response.text)

	# レスポンスを確認
	if not (j.get('issuer') == 'accounts.google.com'):
		return None
	if not (j.get('issued_to') == client_id):
		return None
	if not (j.get('audience') == client_id):
		return None
	email = j.get('email')
	print 'id_token [{0}] is valid. (user is [{1}])'.format(id_token, email)
	return email

# https://accounts.google.com/o/oauth2/revoke?token=xxxxxxxxx
