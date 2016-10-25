# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('role', models.CharField(choices=[('ad', 'Admin'), ('me', 'Member')], max_length=2, default='me')),
                ('team', models.ForeignKey(to='teams.Team', related_name='membership')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='membership')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(through='teams.Membership', to=settings.AUTH_USER_MODEL),
        ),
    ]
