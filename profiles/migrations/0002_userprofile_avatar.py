# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to=profiles.models.user_avatar_path),
        ),
    ]
