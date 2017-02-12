import braintree

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import AddFundsForm
from profiles.models import Wallet


@login_required
def add_funds(request):
    """
    In this view the User can add funds to his wallet.
    """
    if request.method == 'POST':
        form = AddFundsForm(request.POST)
        if form.is_valid():

            wallet = Wallet.objects.get(user=request.user)
            wallet.add_funds(form.cleaned_data['amount'])
            wallet.save()

            messages.add_message(request, messages.SUCCESS, 'Funds added correctly.')

            return redirect('profile')

    else:
        form = AddFundsForm()

    client_token = braintree.ClientToken.generate()

    context = {
        'client_token': client_token,
        'form': form,
    }

    return render(request, 'payments/add_funds.html', context)
