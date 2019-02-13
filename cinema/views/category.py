from django.shortcuts import render,get_object_or_404,redirect
from cinema.models.movies import Movies
from cinema.models.category import Category
from cinema.models.comments import Comments
from cinema.models.likes import Likes
from django.core.paginator import Paginator


def Get_Category(request):
    category_id = request.POST.get('category')

    return redirect('Home')

