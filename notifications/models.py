from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

from teams.models import Team


class Notification(models.Model):

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    user = models.ForeignKey(User)

    def __str__(self):
        return 'Notification: {}'.format(self.user)

    def get_template(self):
        return '{}/{}.html'.format(self.content_object._meta.app_label, self.content_object._meta.model_name)


class TeamInviteNotification(models.Model):

    team = models.ForeignKey(Team)
