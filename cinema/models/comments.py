from django.db import models
from .movies import Movies

class Comments (models.Model):

    comment = models.TextField(max_length=200)

    comment_movie = models.ForeignKey(Movies,on_delete=models.CASCADE)


    def __str__(self):
        return self.comment