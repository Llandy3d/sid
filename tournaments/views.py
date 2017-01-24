from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404

from teams.models import Membership
from .models import Tournament, TournamentEntry


def check_leader_team(user):
    """
    Returns True if the user is the leader of a Team.
    False otherwise.
    """

    memberships = Membership.objects.filter(user=user, role=Membership.ADMIN)
    is_leader = len(memberships) > 0
    return is_leader


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


@login_required
@user_passes_test(check_leader_team, redirect_field_name=None)
def tournament_join(request, tournament_id):
    """
    Page where a Team can join a Tournament.
    """

    tournament_object = get_object_or_404(Tournament, id=tournament_id)
    return render(request, 'tournaments/tournament_join.html', {'tournament': tournament_object})
