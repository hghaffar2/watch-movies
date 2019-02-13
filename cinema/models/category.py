from django.db import models
# from .movies import Movies

class Category(models.Model):

    name = models.CharField(max_length=15)

    # movies = models.ManyToManyField(Movies)


    def __str__(self):
        return self.name