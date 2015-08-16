# coding: utf-8
#
#
# top のビュー。class based にしてみた
#
#
#
#
#

import django
import logging
import subprocess
import time
import inspect
from app1.utils import *
from app1.views import *
from app1.models import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

logger = logging.getLogger(__name__)

class top_views_default(my_abstract_view):

	template_name = 'top/show.html'

	@method_decorator(login_required)
	def get(self, request):

		# *********************************************************************
		# *********************************************************************
		# *********************************************************************
		#
		#
		# netstat の状態を表示するアクション
		#
		#
		# *********************************************************************
		# *********************************************************************
		# *********************************************************************

		logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> $$$ start $$$');

		# =====================================================================
		# setup	
		# =====================================================================	

		# =====================================================================
		# validation	
		# =====================================================================	

		# =====================================================================
		# process
		# =====================================================================

		# =====================================================================
		# contents
		# =====================================================================
		fields = {}
		fields['form'] = {
		}
		fields['window_title'] = 'TOP'
		util.fill_menu_items(request, fields)
		context = django.template.RequestContext(request, fields)
		template = django.template.loader.get_template(self.template_name)
		logger.info('<' + __name__ + '.' + inspect.getframeinfo(inspect.currentframe()).function + '()> --- end ---');
		return django.http.HttpResponse(template.render(context))

class top_views_content(my_abstract_view):

	template_name = 'top/content.html'

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return django.http.HttpResponse('{}')
		return super(top_views_content, self).get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return django.http.HttpResponse('{}')
		return super(top_views_content, self).post(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		fields = {}
		result = Top().get()
		fields['form'] = {
			'lines': result,
		}
		return fields
