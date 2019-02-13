from django.shortcuts import render,get_object_or_404,redirect
from cinema.models.movies import Movies
from cinema.models.likes import Likes

def Like(request):

    like_movie = Likes()
    like_movie.like_movie = get_object_or_404(Movies,pk=request.POST.get('movie_id'))

    like_movie.save()

    return redirect('GetMovie',request.POST.get('movie_id'))