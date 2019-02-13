from django.db import models
from .movies import Movies


class Likes (models.Model):

    like_movie = models.ForeignKey(Movies,on_delete=models.CASCADE)