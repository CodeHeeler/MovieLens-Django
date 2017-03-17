from django.conf.urls import url

from . import views

urlpatterns = [
    # GET /recommender/
    url(r'^$', views.index, name='index'),
    # # GET /recommender/login/
    # url(r'^login/$', views.login, name='login'),
    # # GET /recommender/login_success/
    # url(r'^login_success/$', views.login_success, name='login_success'),

    # GET /recommender/movies/
    url(r'^movies/$', views.movies, name='movies'),
    # GET /recommender/movies/5/
    url(r'^movies/(?P<movie_id>[0-9]+)/$', views.movie_detail, name='movie_detail'),
    # GET /recommender/movie/5/
    url(r'^users/$', views.users, name='users'),
    # GET /recommender/users/5/
    url(r'^users/(?P<user_id>[0-9]+)$', views.user_detail, name='user_detail'),
    # GET /recommender/movies/5/rating/
    url(r'^movies/(?P<movie_id>[0-9]+)/ratings/$', views.ratings, name='ratings'),
    # GET /recommender/movies/5/rate/
    url(r'^(?P<movie_id>[0-9]+)/rate/$', views.rate, name='rate')

    # # GET /recommender/login_error/
    # url(r'^login_error/$', views.login_error, name='login_error')
]
