from django.db import models


class Photo(models.Model):
    name = models.CharField(max_length=200)
    url = models.ImageField(upload_to='photos')

    def show_img(self):
        return """
            <img src="%s" width="150" />
        """ % self.url.url

    show_img.allow_tags = True

    def __unicode__(self):
        return self.name
