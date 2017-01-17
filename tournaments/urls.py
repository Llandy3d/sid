from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.tournaments, name='tournaments'),
    url(r'^(?P<tournament_id>[0-9]+)/$', views.tournament, name='tournament'),
]
