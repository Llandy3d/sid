from django import forms

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

        # TODO raise a ValidationError if each member + team are not different
        cleaned_data = super().clean()
        return cleaned_data
