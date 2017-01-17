# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20161025_2129'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=80)),
                ('starting_date', models.DateTimeField()),
                ('finished', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TournamentEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('coach', models.ForeignKey(related_name='unused_6', to=settings.AUTH_USER_MODEL)),
                ('member_1', models.ForeignKey(related_name='unused_1', to=settings.AUTH_USER_MODEL)),
                ('member_2', models.ForeignKey(related_name='unused_2', to=settings.AUTH_USER_MODEL)),
                ('member_3', models.ForeignKey(related_name='unused_3', to=settings.AUTH_USER_MODEL)),
                ('member_4', models.ForeignKey(related_name='unused_4', to=settings.AUTH_USER_MODEL)),
                ('member_5', models.ForeignKey(related_name='unused_5', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(related_name='tournament_entry', to='teams.Team')),
                ('tournament', models.ForeignKey(related_name='tournament_entry', to='tournaments.Tournament')),
            ],
        ),
        migrations.AddField(
            model_name='tournament',
            name='teams',
            field=models.ManyToManyField(through='tournaments.TournamentEntry', to='teams.Team'),
        ),
        migrations.AlterUniqueTogether(
            name='tournamententry',
            unique_together=set([('member_1', 'member_2', 'member_3', 'member_4', 'member_5', 'coach', 'tournament')]),
        ),
    ]
