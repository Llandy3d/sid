from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.team, name='team'),
    url(r'^create_team/$', views.create_team, name='create_team'),
]
