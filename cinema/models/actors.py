from django.db import models
# from .movies import Movies

class Actors(models.Model):

    real_name = models.CharField(max_length=20)

    photo = models.ImageField(upload_to='photos/')

    movie_name = models.CharField(max_length=20)



    # movies = models.ManyToManyField(Movies)

    def __str__(self):
        return self.real_name
