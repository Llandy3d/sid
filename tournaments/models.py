from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

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

    def get_absolute_url(self):
        return reverse('tournament', args=[str(self.id)])


class TournamentEntry(models.Model):
    """
    Represents a Team Entry into a Tournament.
    Holds extra informations about the partecipants. (chosen members, coach)

    Members have a related_name=unused_* , used to avoid the "clashes with reverse accessor for" error.
    """

    class Meta:
        unique_together = (
            'tournament',
            'team',
        )

    tournament = models.ForeignKey(Tournament, related_name='tournament_entry')
    team = models.ForeignKey(Team, related_name='tournament_entry')
    member_1 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='unused_1')
    member_2 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='unused_2')
    member_3 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='unused_3')
    member_4 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='unused_4')
    member_5 = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='unused_5')
    coach = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='unused_6')

    def pay_fee(self, amount):
        """For each of the selected members pay the fee for the Tournament. The coach doesn't pay."""
        members = [
            self.member_1,
            self.member_2,
            self.member_3,
            self.member_4,
            self.member_5,
        ]

        for member in members:
            member.wallet.remove_funds(amount)
