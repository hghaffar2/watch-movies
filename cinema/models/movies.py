from django.db import models
from .actors import Actors
from .category import Category

class Movies (models.Model):

    name = models.CharField(max_length=20)

    year = models.DateField()

    poster = models.ImageField(upload_to='photos/')

    trailer = models.FileField(upload_to='videos/')

    cast = models.ManyToManyField(Actors)

    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

    def date(self):
        return self.year.strftime('%Y')

