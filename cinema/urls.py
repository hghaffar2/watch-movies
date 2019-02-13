from django.urls import path, include
from .views import actors,category,likes,movies,comments


urlpatterns = [

                        # movies

    path('',movies.Home_view,name='Home'),
    path('details/<int:movie_id>', movies.Details, name='GetMovie'),
    path('newMovie/', movies.Add_movie, name='AddMovie'),
    path('Movie/Delete', movies.Delete_movie , name='DelMovie'),
    path('Movie/SaveEdit',movies.Edit_movie , name='UpMovie'),
    path('Movie/SubmitEdit', movies.Submit_movie, name='SubMovie'),
    path('movie/search' , movies.Search , name='SearchData'),

                        # Comments

    path('movie/comment',comments.Comment,name='Comment'),

                        # Likes

    path('movie/like', likes.Like , name='LikeMovie'),

    path('category/' , category.Get_Category, name='GetCategory' ),

]