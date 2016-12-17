from django.contrib import admin

from .models import Notification, TeamInviteNotification


admin.site.register(Notification)
admin.site.register(TeamInviteNotification)
