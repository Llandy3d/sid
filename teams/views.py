from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from notifications.models import Notification, TeamInviteNotification

from .models import Membership, Team
from .forms import TeamForm, AddMemberForm


@login_required
def team(request):
    """
    Main Team page.
    """

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
    """
    Page for the creation of a new Team.
    A new Membership object will be created for the User creating the Team with role ADMIN.
    """

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
    """
    Page for the invitation of a new member.
    A new Notification object will be created with a TeamInviteNotification.
    """

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


@login_required
def leave_team(request):
    """
    Endpoint for leaving the team, if the User is the leader of the team
    he may not leave the team before giving leadership to someone else.

    NOTE:  It assumes that an User can only have a Membership to only one Team.
    """
    if request.method == 'POST':

        membership = Membership.objects.get(user=request.user)

        if membership.role == Membership.ADMIN:
            messages.add_message(
                request,
                messages.ERROR,
                "You can't leave the team as a Leader. Please transfer leadership before leaving")
            return redirect('team')

        # if it's not the leader of the team
        membership.delete()
        messages.add_message(request, messages.SUCCESS, 'You left the team.')
        return redirect('team')

    return redirect('team')
