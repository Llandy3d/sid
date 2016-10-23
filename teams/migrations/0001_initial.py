# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import teams.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('logo', models.ImageField(default='default.jpg', upload_to=teams.models.team_logo_path)),
            ],
        ),
    ]
