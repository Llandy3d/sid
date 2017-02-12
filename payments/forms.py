import braintree

from django import forms

from .choices import PAYMENT_CHOICES


class AddFundsForm(forms.Form):
    """
    This form is used for adding funds to the wallet.

    The payment_method_nonce field is not set as required because it will be handled in the clean
    method with a custom exception message.
    """

    amount = forms.ChoiceField(choices=PAYMENT_CHOICES, required=True)
    payment_method_nonce = forms.CharField(max_length=1000, widget=forms.widgets.HiddenInput, required=False)

    def clean(self):
        """Try the transaction, if it fails rise a ValidationError."""

        cleaned_data = super().clean()

        payment_method_nonce = cleaned_data.get('payment_method_nonce')
        amount = cleaned_data.get('amount')

        if not payment_method_nonce:
            raise forms.ValidationError("The payment wasn't verified, please try again.")

        if payment_method_nonce and amount:
            result = braintree.Transaction.sale({
                'amount': amount,
                'payment_method_nonce': payment_method_nonce,
                'options': {
                    'submit_for_settlement': True,
                }
            })

            if not result.is_success:
                raise forms.ValidationError(
                    "The payment could have not been processed, please ensure you have enough funds."
                )

        return cleaned_data
