from django.db import models
from django.conf import settings

from teams.models import Team


class Tournament(models.Model):
    """
    Represents a Tournament.
    It is associated with Teams with a many to many through relationship.
    """

    name = models.CharField(max_length=80)
    starting_date = models.DateTimeField()
    teams = models.ManyToManyField(Team, through='TournamentEntry')
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class TournamentEntry(models.Model):
    """
    Represents a Team Entry into a Tournament.
    Holds extra informations about the partecipants. (chosen members, coach)
    """

    tournament = models.ForeignKey(Tournament, related_name='tournament_entry')
    team = models.ForeignKey(Team, related_name='tournament_entry')
    member_1 = models.ForeignKey(settings.AUTH_USER_MODEL)
    member_2 = models.ForeignKey(settings.AUTH_USER_MODEL)
    member_3 = models.ForeignKey(settings.AUTH_USER_MODEL)
    member_4 = models.ForeignKey(settings.AUTH_USER_MODEL)
    member_5 = models.ForeignKey(settings.AUTH_USER_MODEL)
    coach = models.ForeignKey(settings.AUTH_USER_MODEL)
