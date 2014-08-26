# coding: utf-8
from django import forms

class UserForm(forms.Form):

	user_id = forms.CharField(initial='', label='', required=True, help_text='')
	password = forms.CharField(initial='', label='', required=False, help_text='')
	first_name = forms.CharField(initial='', label='', required=False, help_text='')
	last_name = forms.CharField(initial='', label='', required=False, help_text='')
	mail = forms.CharField(initial='', label='', required=False, help_text='')
