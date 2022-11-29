
from django.shortcuts import render, get_object_or_404
from movie import models


def movie_list(request):
    movie = models.Movie.objects.all()
    return render(request, 'movie_list.html', context={'movie': movie})


def movie_detail(request, id):
    movie_id = get_object_or_404(models.Movie, id=id)
    return render(request, 'movie_detail.html', {'movie_id': movie_id})

