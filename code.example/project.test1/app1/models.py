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

# Create your models here.



class Person(models.Model):

	user_id = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	mail = models.CharField(max_length=1000)
	password = models.CharField(max_length=1000)

class ChatMessage(models.Model):

	user_id = models.CharField(max_length=100)
	time_posted = models.DateTimeField()
	message_text = models.CharField(max_length=1000)

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
