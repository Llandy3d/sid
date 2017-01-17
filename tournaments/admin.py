from django.contrib import admin

from .models import Tournament, TournamentEntry


admin.site.register(Tournament)
admin.site.register(TournamentEntry)
