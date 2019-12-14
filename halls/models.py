from django.db import models

# Create your models here.

class Hall(models.Model):
    title = models.CharField(max_length = 200)

class Video(models.Model):
    title = models.CharField(max_length = 200)
    url = models.URLField()
    youtube_id = models.CharField(max_length= 300)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)