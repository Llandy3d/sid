from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def test_view(request):
    return render(request, 'profiles/index.html')


@login_required
def profile(request):
    return render(request, 'profiles/profile.html')
