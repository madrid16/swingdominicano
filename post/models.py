from django.db import models

class post(models.Model):
	text = models.TextField(max_length=300)
	date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.text