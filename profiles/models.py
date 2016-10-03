from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User


# TODO add billing information
class UserProfile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')

    def __str__(self):
        return self.user.username + "'s profile"


class Wallet(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='wallet')
    retirable = models.IntegerField(default=0)
    not_retirable = models.IntegerField(default=0)

    def get_total(self):
        """Returns the total value of the wallet, sum of retirable + not_retirable"""
        return self.retirable + self.not_retirable

    def __str__(self):
        return self.user.username + "'s wallet"


# SIGNALS
def complete_user_profile(sender, instance, **kwargs):
    """After the user is created, create the UserProfile and Wallet"""
    UserProfile.objects.create(user=instance)
    Wallet.objects.create(user=instance)

post_save.connect(complete_user_profile, sender=User)
