# encoding: utf-8

"""
WSGI config for project1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project1.settings")

#
# 「ImportError: No module named app1」というエラーを回避するために挿入した。検証中。
#
import sys
sys.path.append('/django-applications/project1')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
