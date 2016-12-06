from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Membership, Team
from .forms import TeamForm

@login_required
def team(request):

    player_team = None  # initialize
    # There is atleast one membership
    has_team = len(Membership.objects.filter(user=request.user)) > 0
    if has_team:
        player_team = Membership.objects.filter(user=request.user)[0].team

    context = {
        'has_team': has_team,
        'team': player_team,
    }

    return render(request, 'teams/team.html', context)


@login_required
def create_team(request):

    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            new_team = form.save()

            # add the user to the team
            Membership.objects.create(user=request.user, team=new_team, role=Membership.ADMIN)

            return redirect('team')

    # if it's a get
    else:
        form = TeamForm()

    return render(request, 'teams/create_team.html', {'form': form})
