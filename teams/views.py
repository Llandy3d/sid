from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from notifications.models import Notification, TeamInviteNotification

from .models import Membership, Team
from .forms import TeamForm, AddMemberForm


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


@login_required
def add_team_member(request):

    if request.method == 'POST':
        form = AddMemberForm(request.POST)
        if form.is_valid():
            # create the TeamInvite notification and a notification
            user_to_invite = form.cleaned_data['user_to_invite']
            team = Team.objects.get(membership__user=request.user, membership__role=Membership.ADMIN)
            team_invite = TeamInviteNotification.objects.create(team=team)
            Notification.objects.create(content_object=team_invite, user=user_to_invite)

            messages.add_message(request, messages.SUCCESS, 'Invite sent correctly')

            return redirect('team')

    else:
        form = AddMemberForm()

    return render(request, 'teams/add_member.html', {'form': form})
