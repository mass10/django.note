# coding: utf-8
from django import forms

class LoginForm(forms.Form):

	user_id = forms.CharField(initial='', label='', required=True, help_text='', max_length=99)
	password = forms.CharField(initial='', label='', required=False, help_text='')
