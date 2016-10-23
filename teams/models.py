from django.db import models
from django.conf import settings


def team_logo_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/team_<id>/<filename>
    return 'team_{0}/{1}'.format(instance.id, filename)


class Team(models.Model):

    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to=team_logo_path, default='default.jpg')

    def __str__(self):
        return self.name
