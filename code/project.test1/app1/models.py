# coding: utf-8
import django
from django.db import models
from django.utils import timezone
import project1
import json
import os
import sqlite3
import subprocess
import mysql.connector
import datetime
import uuid
from django.forms.models import model_to_dict

# Create your models here.



class Person(models.Model):

	user_id = models.CharField(null=False, max_length=100)
	first_name = models.CharField(null=False, max_length=100)
	last_name = models.CharField(null=False, max_length=100)
	mail = models.CharField(null=False, max_length=1000)
	password = models.CharField(null=False, max_length=1000)

class ChatMessage(models.Model):

	user_id = models.CharField(null=False, max_length=100)
	time_posted = models.DateTimeField(null=False)
	message_text = models.CharField(null=False, max_length=1000)

	# これでも ORDER BY のように働く
	# class Meta:
	# 	ordering =  [ '-time_posted' ]

class PersonManager(models.Manager):

	def list_all(self):

		return Person.objects.all()

	def create_new(self):

		# 正しくは
		# Person.objects.create(name=value, ...)

		# どうしてもデータベースを開きたい場合...
		# path = project1.settings.DATABASES['default']['NAME']
		# connection = sqlite3.connect(path, isolation_level=None)
		# try:
		# 	rows = connection.execute(
		# 		'select mail from app1_person order by 1')
		# 	result = []
		# 	for row in rows:
		# 		result.append(row[0])
		# 	return result
		# except:
		# 	connection.close()
		# 	raise

		pass

class ChatMessageManager(models.Manager):

	def all(self):

		return ChatMessage.objects.all().order_by('-time_posted')

	def create_new(self, user_id, message_text):

		# 新しいメッセージの登録
		new_message = ChatMessage.objects.create(
			user_id=user_id,
			message_text=message_text,
			time_posted=django.utils.timezone.now())
		new_message.save()

class Top:

	def get(self):

		command_text = [
			'sudo', '-u', 'root',
			os.path.join(project1.settings.BASE_DIR, 'bin/top.py')]
		stream = subprocess.Popen(
			command_text,
			shell=False,
			stdout=subprocess.PIPE).stdout
		result = json.load(stream)
		stream.close()
		return result

class Fusen(models.Model):

	fusen_id = models.CharField(null=False, max_length=100)
	order = models.IntegerField(null=False)
	left = models.IntegerField(null=False)
	top = models.IntegerField(null=False)
	width = models.IntegerField(null=False)
	height = models.IntegerField(null=False)
	content = models.TextField(null=True)
	dragging_user_id = models.CharField(null=True, max_length=100)
	time_dragged = models.DateTimeField(null=True)
	user_id_created = models.CharField(null=True, max_length=100)
	user_id_updated = models.CharField(null=True, max_length=100)
	time_created = models.DateTimeField(null=True)
	time_updated = models.DateTimeField(null=True)

	@staticmethod
	def _format_datetime(t):
		if t is None:
			return None
		return t.isoformat()

	def as_dict(self):
		result = {
			'id': self.id,
			'fusen_id': self.fusen_id,
			'order': self.order,
			'left': self.left,
			'top': self.top,
			'width': self.width,
			'height': self.height,
			'content': self.content,
			'dragging_user_id': self.dragging_user_id,
			'time_dragged': Fusen._format_datetime(self.time_dragged),
			'user_id_created': self.user_id_created,
			'user_id_updated': self.user_id_updated,
			'time_created': Fusen._format_datetime(self.time_created),
			'time_updated': Fusen._format_datetime(self.time_updated)
		}
		return result

class FusenManager(models.Manager):

	#
	# from app1.models import *
	# FusenManager().create_new('root', 'test test test test test test')
	#

	# 全ての付箋を抽出
	def all(self):

		return Fusen.objects.all().order_by('-time_updated')

	# 新しい付箋の登録
	def create_new(self, user_id, content):

		newid = uuid.uuid1()
		newid = str(newid)
		new_fusen = Fusen.objects.create(
			fusen_id=newid,
			order=0,
			width=200,
			height=200,
			left=0,
			top=0,
			content=content,
			user_id_created=user_id,
			time_created=django.utils.timezone.now())
		new_fusen.save()
