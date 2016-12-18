from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from teams.models import Membership, Team

from .models import Notification, TeamInviteNotification


@login_required
def notifications(request):
    """
    Shows all the notifications.
    """

    notifications_list = Notification.objects.filter(user=request.user)

    return render(request, 'notifications/notifications.html', {'notifications': notifications_list})


@login_required
def accept_team_invite(request):
    """
    Team invite accepted.
    Membership created for the User.
    Remaining Notifications -> TeamInviteNotification objects removed.
    """
    team_id = request.POST.get('team_id')
    team = Team.objects.get(id=team_id)
    Membership.objects.create(user=request.user, team=team)

    TeamInviteNotification.objects.filter(notifications__user=request.user).delete()

    return redirect('team')


@login_required
def decline_team_invite(request):
    """
    Team invite declined.
    """
