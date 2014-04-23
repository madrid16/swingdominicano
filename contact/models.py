#encoding:utf-8
from django.db import models

class contact(models.Model):
	name = models.CharField(max_length=200)
	number = models.CharField(max_length=10)
	email = models.CharField(max_length=200)
	subject = models.CharField(max_length=200)
	message = models.TextField(max_length=300)
	date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.name