from django.urls import path
from . import views

urlpatterns = [
    path('movie/', views.movie_list, name="movie"),
    path('movie/<int:id>/', views.movie_detail, name="movie_id"),
]

