from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from mr_app.models import Movie, Rater, Rating
from datetime import datetime
import simplejson as json
from django.forms.models import model_to_dict


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

def movie_api_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        release_date = request.POST.get('release_date')
        video_date = request.POST.get('video_date')
        url = request.POST.get('url')

        new_movie = Movie.objects.create(title=title, release_date=release_date,
                                         video_date=video_date, url=url)
        new_movie_dict = model_to_dict(new_movie)

        return HttpResponse(json.dumps(new_movie_dict), content_type='application/json', status=201)

    data = list(Movie.objects.all().values())
    return HttpResponse(json.dumps(data), content_type='application/json')

def rater_api_view(request):
    if request.method == 'POST':
        age = request.POST.get('age')
        occupation = request.POST.get('occupation')
        zipcode = request.POST.get('zipcode')
        sex = request.POST.get('sex')
        new_rater = Rater.objects.create(age=age, occupation=occupation,
                                         zipcode=zipcode, sex=sex)
        new_rater_dict = model_to_dict(new_rater)

        return HttpResponse(json.dumps(new_rater_dict), content_type='application/json', status=201)

    data = list(Rater.objects.all().values())
    return HttpResponse(json.dumps(data), content_type='application/json')

def rating_api_view(request):
    if request.method == 'POST':
        movie_id = request.POST.get('movie_id')
        rating = request.POST.get('rating')
        rater_id = request.POST.get('rater_id')
        timestamp = request.POST.get('timestamp')
        new_rating = Rating.objects.create(movie_id=movie_id, rating=rating, rater_id=rater_id, timestamp=timestamp)
        new_rating_dict = model_to_dict(new_rating)

        return HttpResponse(json.dumps(new_rating_dict), content_type='application/json', status=201)

    data = list(Rating.objects.all().values())
    return HttpResponse(json.dumps(data), content_type='application/json')

def specific_movie_api_view(request, pk):
    if request.method == 'PATCH':
        pass

    elif request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()

    data = list(Movie.objects.filter(pk=pk).values())
    return HttpResponse(json.dumps(data), content_type='application/json')

def specific_rater_api_view(request, pk):
    data = list(Rater.objects.filter(pk=pk).values())
    return HttpResponse(json.dumps(data), content_type='application/json')

def specific_rating_api_view(request, pk):
    data = list(Rating.objects.filter(pk=pk).values())
    return HttpResponse(json.dumps(data), content_type='application/json')

