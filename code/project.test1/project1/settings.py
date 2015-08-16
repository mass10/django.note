# coding: utf-8

"""
Django settings for project1 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2y_a)bnxyjuy-+04v+&o&^5er6ob18g2(#ko!9c&pe%73g2=#p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'app1',

	# httpd 連携する時ははずすこと！
	# 'debug_toolbar',
)

AUTHENTICATION_BACKENDS = (
	'project1.backends.EmailLoginModel',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.locale.LocaleMiddleware',

	# 特にいらないっぽい...
	# 'debug_toolbar.middleware.DebugToolbarMiddleware',
)


#
# 必要無いようだ... デフォルトが採用される？
#
# DEBUG_TOOLBAR_PANELS = (
# 	'debug_toolbar.panels.versions.VersionsPanel',
# 	'debug_toolbar.panels.timer.TimerPanel',
# 	'debug_toolbar.panels.settings.SettingsPanel',
# 	'debug_toolbar.panels.headers.HeadersPanel',
# 	'debug_toolbar.panels.request.RequestPanel',
# 	'debug_toolbar.panels.sql.SQLPanel',
# 	'debug_toolbar.panels.staticfiles.StaticFilesPanel',
# 	'debug_toolbar.panels.templates.TemplatesPanel',
# 	'debug_toolbar.panels.cache.CachePanel',
# 	'debug_toolbar.panels.signals.SignalsPanel',
# 	'debug_toolbar.panels.logging.LoggingPanel',
# 	'debug_toolbar.panels.redirects.RedirectsPanel',
# )

def custom_show_toolbar(request):
	return True

DEBUG_TOOLBAR_CONFIG = {
	'ENABLE_STACKTRACES' : True,
	'SHOW_TOOLBAR_CALLBACK': 'project1.settings.custom_show_toolbar',
}







ROOT_URLCONF = 'project1.urls'

WSGI_APPLICATION = 'project1.wsgi.application'

#
# ロギングを利用するために追記した
#
LOGGING = {
	'version': 1,
	'disable_existing_loggers': True,
	'formatters': {
		'verbose': {
			'format': '%(asctime)s [%(levelname)s] (pid:%(process)d) (thread:%(thread)d) <%(module)s> %(message)s'
		},
		'simple': {
			'format': '%(levelname)s %(message)s'
		},
	},
	'filters': {
	},
	'handlers': {
		'null': {
			'level':'DEBUG',
			'class':'django.utils.log.NullHandler',
		},
		'logfile': {
			'level': 'DEBUG',
			'class':'logging.handlers.WatchedFileHandler',
			'filename': '/var/log/django/application.log',
			'formatter': 'verbose',
		},
		'console': {
			'level':'DEBUG',
			'class':'logging.StreamHandler',
			'formatter': 'verbose',
		},
	},
	'loggers': {
		'app1': {
			'handlers': ['logfile'],
			'level': 'DEBUG',
		},
	}
}

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {

	#
	# SQLite3
	#
	'xxxxxxxxxxxxxxxxxx': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
	},

	#
	# MySQL
	#
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'project1db',
		'USER': 'maaas',
		'PASSWORD': 'pass',
		'HOST': '127.0.0.1',
		'PORT': '3306',
	}
}

#
# リクエスト URL の終端に '/' を付加しない
#
APPEND_SLASH = False

#
# cookie に関するパラメータを追記した
#
# SESSION_COOKIE_AGE = -1 #sec
SESSION_COOKIE_NAME = 'sessionid'

#
# セッションの実装に何を選択するか
#
# SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

#
# in-memory session を利用するために追記した
#    -> 消した
CACHES = {
	'default' : {
		# 'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
		# 'LOCATION': 'WE ARE THE WORLD'
		'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
		'LOCATION': '127.0.0.1:11211'
	}
}

#
# JavaScript などによる Cookie へのアクセスを禁止する。ただし、実際にどのような挙動をするかはウェブブラウザの実装によるため、これは紳士協定と言える。
#
SESSION_COOKIE_HTTPONLY = True

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

#
# 言語設定
#
LANGUAGE_CODE = 'ja-JP'

#
# タイムゾーン
#
TIME_ZONE = 'Japan'
USE_TZ = True

#
# 国際化対応
#
USE_I18N = True
USE_L10N = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

#
# 静的コンテンツへのパス
#
STATIC_URL = '/static/'

#
# デフォルト文字セット(utf-8)
# ドキュメンテーション: 「DEFAULT_CHARSET に依存したコードを書いてはならない」
#
# DEFAULT_CHARSET

#
# 試験中...
#
# LOCALE_PATHS = (
# 	os.path.join(BASE_DIR, 'app1/locale/')
# )

#
# 認証が済んでいないセッションによるアクセスに対して見せるページ
#
LOGIN_URL = '/login'
