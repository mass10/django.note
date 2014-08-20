# coding: utf-8
#
# カスタムフィルタの実装例
#

from django import template

register = template.Library()

@register.filter()
def nn(value):

	if value is None:
		return ''
	
	return value
