# coding: utf-8
from django import forms

class UserForm(forms.Form):

	user_id = forms.CharField(initial='', label='', required=True, help_text='')
	group_id = forms.CharField(initial='', label='', help_text='')
	password = forms.CharField(initial='', label='', required=True, help_text='')
	mail = forms.CharField(initial='', label='', required=True, help_text='')
