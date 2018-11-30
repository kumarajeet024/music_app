from django.shortcuts import render #this render method for loading the template and
#giving the http respose at the same time.
from django.http import Http404
#from django.template import loader
#from django.http import HttpResponse
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    #template = loader.get_template('music/index.html')
    context = {
    'all_albums':all_albums,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    #return HttpResponse("<h2>Details for album id:" + str(album_id)+"</h2>")

    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'music/detail.html', {'album': album})