from django.db import models

class Video(models.Model):
	code = models.TextField(max_length=300)
	active = models.BooleanField(default=False)

	def __unicode__(self):
		return self.code