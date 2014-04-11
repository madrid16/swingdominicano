# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response

def list_photos(request):
	return render_to_response('list_photos.html', locals())