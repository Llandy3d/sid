# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0003_auto_20170124_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='description',
            field=models.TextField(default='Tournament Description'),
        ),
    ]
