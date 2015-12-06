# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0002_auto_20151205_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='id',
            field=models.CharField(max_length=32, serialize=False, primary_key=True),
        ),
    ]
