from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# from django.template import loader
from django.db.models import Count, Avg
from .models import Movie


def index(request):
    return render(request, 'recommender/index.html')


# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         return render(request, 'recommender/login_success.html')
#     else:
#         # Return an 'invalid login' error message.
#         return render(request, 'recommender/login_error.html')
#     return render(request, 'recommender/login.html')

#
# def login_error(request):
#     #login error stuff
#     return HttpResponse("There was an error with your login.")
#
#
# def login_success(request):
#     #login success stuff
#     return HttpResponse("Success! You are now logged in.")


def top_20(request):
    # if not request.user.is_authenticated:
    #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    top = Movie.objects.annotate(avg=Avg('rating'), rate_count=Count('rating')).order_by('-rate_count')[:20]
    return render(request, 'recommender/top_20.html', {'top20': top})


def movies(request):
    return render(request, 'recommender/movies.html')


def movie_detail(request, movie_id):
    # if not request.user.is_authenticated:
    #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'recommender/movie_detail.html', {'movie': movie, 'num_rating': movie.num_of_ratings(), 'avg': movie.average_rating()})


def users(request):
    return render(request, 'recommender/users.html')


def user_detail(request, user_id):
    # if not request.user.is_authenticated:
    #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'recommender/user_detail.html', {'user': user})


def ratings(request, movie_id):
    # if not request.user.is_authenticated:
    #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    response = "You're looking at the results of movie %s."
    return HttpResponse(response % movie_id)


def rate(request, movie_id):
    # if not request.user.is_authenticated:
    #     return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    return HttpResponse("You're voting on movie %s." % movie_id)
