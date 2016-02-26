from django.shortcuts import render
from django.db.models import Avg
from mr_app.models import Movie, Rater, Rating


def index_view(request):
    # average_ratings = Rating.objects.annotate(avg_rating=Avg('rating'))

    top20 = Movie.objects.all().order_by('-avg_rating')[:20]

    return render(request, 'index.html', {'top20': top20})