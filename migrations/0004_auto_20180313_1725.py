# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartoview_tutorials', '0003_auto_20180313_0355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='is_image',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
