from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Membership

@login_required
def team(request):

    # There is atleast one membership
    has_team = len(Membership.objects.filter(user=request.user)) > 0

    context = {
        'has_team': has_team,
    }

    return render(request, 'teams/team.html', context)
