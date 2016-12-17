from django import forms

from django.contrib.auth.models import User

from .models import Team


class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        exclude = ('members',)


class AddMemberForm(forms.Form):

    # NOTE  Currently the user can get spammed the invites from the same team
    queryset = User.objects.filter(membership=None)
    user_to_invite = forms.ModelChoiceField(queryset=queryset)
