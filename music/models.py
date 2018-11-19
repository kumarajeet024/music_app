from django.db import models

# Create your models here.
class Album(models.Model):
     artist = models.CharField(max_length=250)
     album_title = models.CharField(max_length=500)
     genre = models.CharField(max_length=100)
     album_logo = models.CharField(max_length=1000)

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    #album is used as foreign key that connects Album and Song by unique id.
    #each Album have unique id no.
    #on_delete = models.CASCADE means on deleting the album the songs linked to them gets deleted.
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)