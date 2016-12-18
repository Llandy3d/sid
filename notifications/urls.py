from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.notifications, name='notifications'),

    url(r'^accept-team-invite/$', views.accept_team_invite, name='accept_team_invite'),
    url(r'^decline-team-invite/$', views.decline_team_invite, name='decline_team_invite'),
]
