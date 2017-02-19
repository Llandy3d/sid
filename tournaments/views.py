from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from teams.models import Membership
from .models import Tournament, TournamentEntry
from .forms import JoinTournamentForm


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
    team = Membership.objects.get(user=request.user, role=Membership.ADMIN).team

    # If there is already an Entry for this Team, redirect back to the tournament
    tournament_entrys = TournamentEntry.objects.filter(tournament=tournament_object, team=team)
    if len(tournament_entrys) > 0:
        return redirect(tournament_object)

    # TODO revise this, right now it checks if any of the wallet money is >= 5
    member_queryset = User.objects.filter(Q(team=team), Q(wallet__retirable__gte=5) | Q(wallet__not_retirable__gte=5))

    if request.method == 'POST':
        form = JoinTournamentForm(request.POST, member_queryset=member_queryset)
        if form.is_valid():
            tournament_entry = form.save(commit=False)
            tournament_entry.tournament = tournament_object
            tournament_entry.team = team
            tournament_entry.pay_fee(5)  # TODO right now is 5 the cost of a tournament, move it
            tournament_entry.save()

            return redirect(tournament_object)
    else:
        form = JoinTournamentForm(member_queryset=member_queryset)

    return render(request, 'tournaments/tournament_join.html', {'form': form, 'tournament': tournament_object})
