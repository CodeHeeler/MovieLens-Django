from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.CharField(max_length=200)

    def __repr__(self):
        return "{}: {} - {}".format(self.id, self.title, self.release_date)

    def __str__(self):
        return self.__repr__()

    def average_rating(self):
        r = [rate for rate in Rating.objects.all().filter(movie=self.id)]
        all_rating = [rate.rating for rate in r]
        average = sum(all_rating) / len(r)
        return "Average rating: {:0.3f} stars out of 5 ({} ratings)".format(average, len(r))

    def num_of_ratings(self):
        r = [rate for rate in Rating.objects.all().filter(movie=self.id)]
        return len(r)


class User(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=200)

    def __repr__(self):
        return "{}: {}({})".format(self.id, self.age, self.gender)

    def __str__(self):
        return self.__repr__()


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    rating_date = models.CharField(max_length=200)

    def __repr__(self):
        return "Movie: {}, Rating: {}, User: {} - {}".format(self.movie_id, self.rating, self.user_id, self.rating_date)

    def __str__(self):
        return self.__repr__()


# class Genre(models.Model):
#     movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     pub_date = models.DateTimeField('date published')
