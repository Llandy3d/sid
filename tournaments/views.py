from django.shortcuts import render, get_object_or_404

from .models import Tournament


def tournaments(request):
    """
    Page that displays all the Tournaments.
    """

    tournaments_objects = Tournament.objects.all()
    return render(request, 'tournaments/tournaments.html', {'tournaments': tournaments_objects})


def tournament(request, tournament_id):
    """
    Page that displays a single Tournament.
    """

    tournament_object = get_object_or_404(Tournament, id=tournament_id)
    return render(request, 'tournaments/tournament.html', {'tournament': tournament_object})
