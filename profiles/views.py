from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def test_view(request):
    return render(request, 'profiles/index.html')


@login_required
def profile(request):
    """
    User profile page.
    """

    context = {
        'has_steam_connected': request.user.profile.has_steam_connected(),
        'balance': request.user.wallet.get_total(),
    }

    return render(request, 'profiles/profile.html', context)
