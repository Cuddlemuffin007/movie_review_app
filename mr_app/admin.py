from django.contrib import admin
from mr_app.models import Rater, Movie, Rating


admin.site.register([Rater, Movie, Rating])
