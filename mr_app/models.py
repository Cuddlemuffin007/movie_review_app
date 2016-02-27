from django.db import models


class Rater(models.Model):
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    occupation = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=5)

    def __str__(self):
        return "User {} {}{}".format(self.pk, self.age, self.sex)


class Movie(models.Model):
    title = models.TextField()
    release_date = models.CharField(max_length=8)
    video_date = models.CharField(max_length=10, blank=True)
    url = models.URLField()
    unknown = models.BooleanField(default=0)
    action = models.BooleanField(default=0)
    adventure = models.BooleanField(default=0)
    animation = models.BooleanField(default=0)
    childrens = models.BooleanField(default=0)
    comedy = models.BooleanField(default=0)
    crime = models.BooleanField(default=0)
    documentary = models.BooleanField(default=0)
    drama = models.BooleanField(default=0)
    fantasy = models.BooleanField(default=0)
    film_noir = models.BooleanField(default=0)
    horror = models.BooleanField(default=0)
    musical = models.BooleanField(default=0)
    mystery = models.BooleanField(default=0)
    romance = models.BooleanField(default=0)
    scifi = models.BooleanField(default=0)
    thriller = models.BooleanField(default=0)
    war = models.BooleanField(default=0)
    western = models.BooleanField(default=0)
    avg_rating = models.FloatField()

    def __str__(self):
        return "{}".format(self.title[:-7])


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField()
    timestamp = models.IntegerField()

    def __str__(self):
        return "{} Rating: {}".format(self.rater, self.rating)
