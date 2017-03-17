from django.conf.urls import url

from . import views

urlpatterns = [
    # GET /recommender/
    url(r'^$', views.index, name='index'),
    # GET /recommender/5/
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
    # GET /recommender/5/rating/
    url(r'^(?P<movie_id>[0-9]+)/ratings/$', views.ratings, name='ratings'),
    # GET /recommender/5/rate/
    url(r'^(?P<movie_id>[0-9]+)/rate/$', views.rate, name='rate'),
]
