from django.contrib import admin

from .models import UserProfile, Wallet

admin.site.register(UserProfile)
admin.site.register(Wallet)
