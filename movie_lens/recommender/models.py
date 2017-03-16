from django.db import models


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    # release_date = models.DateTimeField('date released')
    release_date = models.CharField(max_length=200)

    def __repr__(self):
        return "{}: {} - {}".format(self.movie_id, self.title, self.release_date)


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=200)

    def __repr__(self):
        return "{}: {}({})".format(self.user_id, self.age, self.gender)


# table is header is formatted funny id, rating, rating_date, movie_id, user_id
class Rating(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    rating_date = models.CharField(max_length=200)
    # rating_date = models.DateTimeField('date published')

    def __repr__(self):
        return "Movie: {}, Rating: {}, User: {} - {}".format(self.movie_id, self.rating, self.user_id, self.rating_date)


# class Genre(models.Model):
#     movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     pub_date = models.DateTimeField('date published')
