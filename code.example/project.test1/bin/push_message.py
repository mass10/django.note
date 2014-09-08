#!/usr/bin/env python
# coding: utf-8
#
# Django ウェブアプリケーションのモデルを利用してチャットメッセージを登録する例
#
#
#
#

import os
import sys
sys.path.append('../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project1.settings")
import django
from django.utils import timezone
import codecs
import project1.settings
from app1.models import *


def _println(*arguments):

	out = codecs.getwriter('utf-8')(sys.stdout)
	for unknown in arguments:
		out.write('' + unknown)
	out.write("\n")

def _main(*argv):

	message_text = u'自動生成されたメッセージです'
	if 1 < len(argv):
		message_text = argv[1]
	ChatMessageManager().create_new(
		u'root', message_text)

_main(*sys.argv)

