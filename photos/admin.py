from django.contrib import admin

from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_img')


admin.site.register(Photo, PhotoAdmin)