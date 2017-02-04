from django import forms
from django.core.exceptions import ValidationError

from .models import TournamentEntry


class JoinTournamentForm(forms.ModelForm):

    class Meta:
        model = TournamentEntry
        fields = (
            # 'tournament', ## excluded because it will be set in the view
            # 'team',       ## excluded because it will be set in the view
            'member_1',
            'member_2',
            'member_3',
            'member_4',
            'member_5',
            'coach',
        )

    def __init__(self, *args, **kwargs):
        # pop the value out before calling super() because it does not expect the kwarg
        member_queryset = kwargs.pop('member_queryset')

        super().__init__(*args, **kwargs)
        self.fields['member_1'].queryset = member_queryset
        self.fields['member_2'].queryset = member_queryset
        self.fields['member_3'].queryset = member_queryset
        self.fields['member_4'].queryset = member_queryset
        self.fields['member_5'].queryset = member_queryset

    def clean(self):
        """
        Raise a ValidationError if the Members selected are not all different from each other.
        """

        cleaned_data = super().clean()

        member_1 = cleaned_data.get('member_1')
        member_2 = cleaned_data.get('member_2')
        member_3 = cleaned_data.get('member_3')
        member_4 = cleaned_data.get('member_4')
        member_5 = cleaned_data.get('member_5')
        coach = cleaned_data.get('coach')

        members_list = [
            member_1,
            member_2,
            member_3,
            member_4,
            member_5,
            coach,
        ]

        for member in members_list:
            frequency = members_list.count(member)
            if frequency > 1:
                raise ValidationError("Each member has to be different")

        return cleaned_data
