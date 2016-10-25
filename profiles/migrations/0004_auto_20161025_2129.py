# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20161023_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_leader',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='team',
        ),
    ]
