from django import forms

from django.contrib.auth.models import User

from .models import Team


class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        exclude = ('members',)


class AddMemberForm(forms.Form):

    user_to_invite = forms.ModelChoiceField(queryset=User.objects.all())
