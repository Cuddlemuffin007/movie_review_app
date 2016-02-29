from django.db.models import Avg
from django.shortcuts import render
from mr_app.models import Movie, Rater, Rating
from datetime import datetime


def index_view(request):
    top20 = Movie.objects.all().order_by('-avg_rating')[:20]

    return render(request, 'index.html', {'top20': top20})

def movie_view(request, re_capture):
    movie = Movie.objects.get(pk=re_capture)
    rater = Rater.objects.get(pk=0)
    rating = request.POST.get('rating')

    if rating and not Rating.objects.filter(movie=movie, rater=rater):
        Rating.objects.create(rater=rater, movie=movie,
                              rating=rating, timestamp=int(datetime.timestamp(datetime.now())))

    # recalculate the movies average rating
    avg_rating = Rating.objects.filter(movie=movie).aggregate(Avg('rating'))
    movie.avg_rating = avg_rating['rating__avg']
    movie.save()

    movie_ratings = Rating.objects.filter(movie=movie.pk).order_by('-timestamp')

    return render(request, 'movie.html', {
                                        'movie': movie,
                                        'ratings': movie_ratings
    })

def rater_view(request, re_capture):
    rater = Rater.objects.get(pk=re_capture)
    rater_movies = Rating.objects.filter(rater=rater.pk).order_by('-timestamp')

    return render(request, 'rater.html', {
                                        'rater': rater,
                                        'rater_movies' : rater_movies
    })

def all_movies(request):
    all_movies = Movie.objects.all().order_by('title')

    return render(request, 'all_movies.html', {'all_movies': all_movies})
