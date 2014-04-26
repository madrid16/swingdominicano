# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from models import Video


def video(request):
    video_principal = Video.objects.filter(active=True).values()[0]
    videos = Video.objects.all().exclude(id=video_principal['id']).values()
    return render_to_response('video.html', locals())
