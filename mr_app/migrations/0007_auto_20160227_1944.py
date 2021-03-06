# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 20:50
from __future__ import unicode_literals

from django.db import migrations
from django.db.models import Avg


def add_avg_rating(apps, schema_editor):
    Movie = apps.get_model('mr_app', 'Movie')
    Rating = apps.get_model('mr_app', 'Rating')

    all_movies = Movie.objects.all()

    for movie in all_movies:
        avg_rating = Rating.objects.filter(movie=movie.pk).aggregate(Avg('rating'))
        movie.avg_rating = avg_rating['rating__avg']
        movie.save()



class Migration(migrations.Migration):

    dependencies = [
        ('mr_app', '0004_movie_avg_rating'),
    ]

    operations = [
        migrations.RunPython(add_avg_rating)
    ]
