from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from movie import models, forms


def movie_list(request):
    movie = models.Movie.objects.all()
    return render(request, 'movie_list.html', context={'movie': movie})


def movie_detail(request, id):
    movie_id = get_object_or_404(models.Movie, id=id)
    return render(request, 'movie_detail.html', {'movie_id': movie_id})


def add_movie(request):
    method = request.method
    if method == 'POST':
        form = forms.MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Movie created')
    else:
        form = forms.MovieForm()
    return render(request, 'add_movie.html', {'form': form})


def movie_update(request, id):
    movie_object = get_object_or_404(models.Movie, id=id)
    if request.method == 'POST':
        form = forms.MovieForm(instance=movie_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Movie Updated Successfully')

    else:
        form = forms.MovieForm(instance=movie_object)
    return render(request, 'movie_update.html', {'form': form, 'object': movie_object})


def movie_delete(request, id):
    movie_object = get_object_or_404(models.Movie, id=id)
    movie_object.delete()
    return HttpResponse('Book Deleted')
