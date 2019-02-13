from django.contrib import admin
from .models.movies import Movies
from .models.category import Category
from .models.actors import Actors
from .models.likes import Likes
from .models.comments import Comments

admin.site.register(Movies)
admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(Actors)
admin.site.register(Likes)
