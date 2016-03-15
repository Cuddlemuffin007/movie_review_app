"""movieratings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mr_app.views import index_view, movie_view, rater_view, all_movies, movie_api_view,\
    rater_api_view, rating_api_view, specific_movie_api_view, specific_rater_api_view, specific_rating_api_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view, name='index_view'),
    url(r'^all$', all_movies, name='all_movies'),
    url(r'^movies/(\d+)$', movie_view, name='movie_view'),
    url(r'^rater/(\d+)$', rater_view, name='rater_view'),
    url(r'^api/movie/$', movie_api_view, name='movie_api_view'),
    url(r'^api/rater/$', rater_api_view, name='rater_api_view'),
    url(r'^api/rating/$', rating_api_view, name='rating_api_view'),
    url(r'^api/movie/(\d+)$', specific_movie_api_view, name='specific_movie_api_view'),
    url(r'^api/rater/(?P<pk>\d+)$', specific_rater_api_view, name='specific_rater_api_view'),
    url(r'^api/rating/(?P<pk>\d+)$', specific_rating_api_view, name='specific_rating_view'),
]
