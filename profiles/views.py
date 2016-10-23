from django.shortcuts import render


def test_view(request):
    # return render(request, 'profiles/index.html')
    return render(request, 'base.html')
