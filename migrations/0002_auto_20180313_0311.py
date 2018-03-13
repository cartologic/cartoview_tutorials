# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cartoview_tutorials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='author',
            field=models.ForeignKey(related_name='tutorials', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
