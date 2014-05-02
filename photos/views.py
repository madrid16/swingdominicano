# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from models import Photo


def list_photos(request):
    photos = Photo.objects.all()
    return render_to_response('list_photos.html', locals())