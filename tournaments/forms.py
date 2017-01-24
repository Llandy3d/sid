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

    def clean(self):

        # TODO raise a ValidationError if each member + team are not different
        cleaned_data = super().clean()
        return cleaned_data
