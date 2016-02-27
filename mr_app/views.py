from django.shortcuts import render
from mr_app.models import Movie, Rater, Rating


def index_view(request):
    top20 = Movie.objects.all().order_by('-avg_rating')[:20]

    return render(request, 'index.html', {'top20': top20})

def movie_view(request, re_capture):
    movie = Movie.objects.get(pk=re_capture)
    movie_ratings = Rating.objects.filter(movie=movie.pk)

    return render(request, 'movie.html', {
                                        'movie': movie,
                                        'ratings': movie_ratings
    })

def rater_view(request, re_capture):
    rater = Rater.objects.get(pk=re_capture)
    rater_movies = Rating.objects.filter(rater=rater.pk)

    return render(request, 'rater.html', {
                                        'rater': rater,
                                        'rater_movies' : rater_movies
    })