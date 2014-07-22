# coding: utf-8
#
# “ÆŽ©ƒtƒBƒ‹ƒ^‚ÌŽÀ‘•—á
#

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter()
def nbsp(value):
	if value == None:
		return 'None'
	return mark_safe(value.replace(' ', '&nbsp;'))
