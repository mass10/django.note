# coding: utf-8
from django import forms

class MessageForm(forms.Form):

	message_text = forms.CharField(initial='', label='', required=True, help_text='')
