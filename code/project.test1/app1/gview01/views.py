# coding: utf-8

import django
import logging
import subprocess
import time
import inspect
from app1.utils import *
from app1.views import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

logger = logging.getLogger(__name__)

class gview01(my_abstract_view):

	template_name = 'gview01/default.html'

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(gview01, self).dispatch(request, *args, **kwargs)
