from django.shortcuts import render,get_object_or_404,redirect
from cinema.models.movies import Movies
from cinema.models.comments import Comments

def Comment(request):

    # movie_id = request.POST.get('movie_id')
    comment = Comments()
    comment.comment = request.POST.get('comment')
    comment.comment_movie = get_object_or_404(Movies,pk=request.POST.get('movie_id'))
    comment.save()

    return redirect('GetMovie',request.POST.get('movie_id'))