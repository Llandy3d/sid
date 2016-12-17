from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

from teams.models import Team


class Notification(models.Model):
    """
    General Notification class that holds the actual notification as a general object.
    """

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    user = models.ForeignKey(User)

    def __str__(self):
        return 'Notification: {}'.format(self.user)

    def get_template(self):
        """
        Returns the appropriate template snippet for the specific Notification model of the content_object,
        'app_label/model_name.html' format
        """
        return '{}/{}.html'.format(self.content_object._meta.app_label, self.content_object._meta.model_name)


class TeamInviteNotification(models.Model):
    """
    Notification that represents a team invite
    """

    team = models.ForeignKey(Team)
