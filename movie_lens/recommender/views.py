from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
# from django.template import loader
from django.db.models import Count, Avg
from .models import Movie


def index(request):
    top = Movie.objects.annotate(avg=Avg('rating'), rate_count=Count('rating')).order_by('-rate_count')[:20]
    return render(request, 'recommender/index.html', {'top20': top})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'recommender/detail.html', {'movie': movie, 'num_rating': movie.num_of_ratings(), 'avg': movie.average_rating()})


def ratings(request, movie_id):
    response = "You're looking at the results of movie %s."
    return HttpResponse(response % movie_id)


def rate(request, movie_id):
    return HttpResponse("You're voting on movie %s." % movie_id)
