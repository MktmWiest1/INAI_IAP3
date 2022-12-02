from django.urls import path
from . import views

urlpatterns = [
    path('movie/', views.movie_list, name="movie"),
    path('movie/<int:id>/', views.movie_detail, name="movie_id"),
    path('movie/<int:id>/update/', views.movie_update, name='movie_update'),
    path('movie/<int:id>/delete/', views.movie_delete, name='movie_delete'),
    path('add-movie/', views.add_movie, name='add_movie')
]

