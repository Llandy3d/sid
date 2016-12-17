from django.db import models
from django.conf import settings


def team_logo_path(instance, filename):
    """
    Returns the path to the Team logo image.
    """
    # file will be uploaded to MEDIA_ROOT/team_<id>/<filename>
    return 'team_{0}/{1}'.format(instance.id, filename)


class Team(models.Model):
    """
    Represents a Team.
    """

    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to=team_logo_path, default='default.jpg')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    """
    Represents the idea of Membership between Users and Teams.
    ROLES: member or admin.
    """

    ADMIN = 'ad'
    MEMBER = 'me'

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (MEMBER, 'Member'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='membership')
    team = models.ForeignKey(Team, related_name='membership')

    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default=MEMBER)
