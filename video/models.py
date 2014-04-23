from django.db import models

class video(models.Model):
	code = models.TextField(max_length=300)

	def __unicode__(self):
		return self.code