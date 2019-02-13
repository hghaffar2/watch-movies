from django.shortcuts import render,get_object_or_404,redirect
from cinema.models.movies import Movies
from cinema.models.category import Category
from cinema.models.comments import Comments
from cinema.models.likes import Likes
from django.core.paginator import Paginator



def Home_view(request):


    movies = Movies.objects.filter().order_by('-year')

    paginator_brands = Paginator(movies, 6)
    page_movie = request.GET.get('page')
    all_movies = paginator_brands.get_page(page_movie)

    categories = Category.objects.all().order_by('name')

    return render(request,'movies/home.html',{'movies':all_movies,'categories':categories})




def Details (request,movie_id):

                        # movie information

    movies = get_object_or_404( Movies , pk=movie_id )

                        # Likes


    movies.likes = Likes.objects.filter(like_movie= movie_id).count()

                        # all comments

    comments = Comments.objects.filter(comment_movie = movie_id)

                        # Function return

    return render(request,'movies/details.html',{ 'movie' : movies , 'comments':comments } )



def Add_movie(request):

    categories = Category.objects.all()

    if request.method == 'POST' :
        newMovie = Movies()
        newMovie.name = request.POST.get('name')
        newMovie.year = request.POST.get('year')
        newMovie.poster = request.FILES['poster']
        newMovie.trailer = request.FILES['trailer']
        get_category = request.POST.get('category')
        newMovie.save()
        newMovie.category.add(get_category)
        return redirect('Home')
    else:
        return render(request,'movies/form_movie.html',{'categories':categories})



def Delete_movie(request):
    movie_id = request.POST.get('movie_id')
    delete_movie = get_object_or_404(Movies,pk=movie_id)
    delete_movie.delete()

    return redirect('Home')



def Submit_movie(request):

    movie_id = request.POST.get('movie_id')

    movie = get_object_or_404(Movies,pk=movie_id)

    categories = Category.objects.all()


    return render(request,'movies/form_movie.html',{'movie': movie,'categories':categories })



def Edit_movie(request):


    movie_id = request.POST.get('movie_id')

    movie = get_object_or_404(Movies,pk=movie_id)
    movie.trailer = request.FILES['trailer']
    movie.poster = request.FILES['poster']
    movie.year = request.POST.get('year')
    movie.name = request.POST.get('name')
    get_category = request.POST.get('category')
    movie.category.add(get_category)

    movie.save()

    return redirect('Home')

def Search(request):

    search = request.POST.get('search')

    if request.POST.get('option') == 'movie' :

        all_movies = Movies.objects.filter( name__icontains = search ).order_by('year')
        categories = Category.objects.all().order_by('name')


    elif request.POST.get('option') == 'category' :

        categories = Category.objects.filter( name__icontains = search ).order_by('name')
        all_movies = Movies.objects.all().order_by('year')

    elif request.POST.get('option') == 'year' :

        all_movies = Movies.objects.filter(year__icontains=search)
        categories = Category.objects.all().order_by('name')

    elif request.POST.get('option') == 'all' :

        all_movies = Movies.objects.filter( name__icontains=search ).order_by('year')
        categories = Category.objects.filter( name__icontains=search ).order_by('name')

    return render(request,'movies/home.html',{'search':search,'movies':all_movies,'categories': categories})




