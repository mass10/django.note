#!/usr/bin/env python
# coding: utf-8
#
# Django ウェブアプリケーションのモデルを利用してレコードを登録する例
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

	content = u'自動生成されたテキストです'
	if 1 < len(argv):
		content = argv[1]
	FusenManager().create_new(
		u'root', content)

_main(*sys.argv)
