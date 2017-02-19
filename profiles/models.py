from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from teams.models import Team


def user_avatar_path(instance, filename):
    """
    Returns the path to the user avatar image.
    """
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


# TODO add billing information
class UserProfile(models.Model):
    """
    Represents the User profile.

    avatar:  The user avatar image
    """

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
    avatar = models.ImageField(upload_to=user_avatar_path, default='default.jpg')

    def has_steam_connected(self):
        """Returns wether the user has connected his steam account"""
        return len(self.user.socialaccount_set.all()) > 0

    def __str__(self):
        return self.user.username + "'s profile"


class Wallet(models.Model):
    """
    User wallet, values divided in retirable and not retirable. The total is formed by their addition.
    """

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='wallet')
    retirable = models.IntegerField(default=0)
    not_retirable = models.IntegerField(default=0)

    def get_total(self):
        """Returns the total value of the wallet, sum of retirable + not_retirable"""
        return self.retirable + self.not_retirable

    def add_funds(self, amount):
        """Add funds to the not_retirable wallet part."""
        # TODO this might need exception checking
        self.not_retirable += int(float(amount))

    def remove_funds(self, amount):
        # TODO right now just removes from not_retirable, add logic to remove from both
        """Remove funds from the wallet."""
        self.not_retirable -= amount

    def __str__(self):
        return self.user.username + "'s wallet"


# SIGNALS
def complete_user_profile(sender, instance, created, **kwargs):
    """After the user is created, create the UserProfile and Wallet"""
    if created:
        UserProfile.objects.create(user=instance)
        Wallet.objects.create(user=instance)

post_save.connect(complete_user_profile, sender=User)
