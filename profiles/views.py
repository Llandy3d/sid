from django.shortcuts import render


def test_view(request):
    return render(request, 'profiles/index.html')
