from django.shortcuts import render

from django.template import loader
from django.http import HttpResponse
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
    'all_albums':all_albums,
    }
    return HttpResponse(template)


def detail(request, album_id):
    return HttpResponse("<h2>Details for album id:" + str(album_id)+"</h2>")