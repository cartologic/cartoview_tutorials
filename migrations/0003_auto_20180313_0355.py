# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cartoview_tutorials.validators
import cartoview_tutorials.models


class Migration(migrations.Migration):

    dependencies = [
        ('cartoview_tutorials', '0002_auto_20180313_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='file',
            field=models.FileField(upload_to=cartoview_tutorials.models.get_tutorial_path, validators=[cartoview_tutorials.validators.validate_file]),
        ),
    ]
