# coding: utf-8
from django.db import models
import project1
import json
import sqlite3

# Create your models here.



class Person(models.Model):

	user_id = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	mail = models.CharField(max_length=1000)
	password = models.CharField(max_length=1000)

class PersonManager(models.Manager):

	def list_all(self):

		path = project1.settings.DATABASES['default']['NAME']
		connection = sqlite3.connect(path, isolation_level=None)
		try:
			rows = connection.execute(
				'select user_id, first_name, last_name, mail from app1_person order by 1')
			result = []
			for row in rows:
				user = {
					'user_id': row[0],
					'first_name': row[1],
					'last_name': row[2],
					'mail': row[3],
				}
				result.append(user)
			return result
		except:
			connection.close()
			raise

	def create_new():

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
