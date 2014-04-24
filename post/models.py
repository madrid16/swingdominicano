from django.db import models
from tinymce.models import HTMLField

class Post(models.Model):
	text = HTMLField()
	date = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return '%s %s' % (self.text, self.date)