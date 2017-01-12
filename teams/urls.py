from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.team, name='team'),
    url(r'^create_team/$', views.create_team, name='create_team'),
    url(r'^add_member/$', views.add_team_member, name='add_member'),
    url(r'^leave-team/$', views.leave_team, name='leave_team'),
]
