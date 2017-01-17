# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamententry',
            name='coach',
            field=models.ForeignKey(related_name='unused_6', to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterField(
            model_name='tournamententry',
            name='member_1',
            field=models.ForeignKey(related_name='unused_1', to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterField(
            model_name='tournamententry',
            name='member_2',
            field=models.ForeignKey(related_name='unused_2', to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterField(
            model_name='tournamententry',
            name='member_3',
            field=models.ForeignKey(related_name='unused_3', to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterField(
            model_name='tournamententry',
            name='member_4',
            field=models.ForeignKey(related_name='unused_4', to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterField(
            model_name='tournamententry',
            name='member_5',
            field=models.ForeignKey(related_name='unused_5', to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='tournamententry',
            unique_together=set([('tournament', 'team')]),
        ),
    ]
