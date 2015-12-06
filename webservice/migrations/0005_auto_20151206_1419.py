# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0004_auto_20151205_1646'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatmessage',
            options={'ordering': ('pubdate',)},
        ),
        migrations.RenameField(
            model_name='chatmessage',
            old_name='message_text',
            new_name='messagetext',
        ),
        migrations.RenameField(
            model_name='chatmessage',
            old_name='pub_date',
            new_name='pubdate',
        ),
        migrations.RenameField(
            model_name='chatmessage',
            old_name='room_text',
            new_name='roomtext',
        ),
        migrations.RenameField(
            model_name='chatmessage',
            old_name='user_text',
            new_name='usertext',
        ),
    ]
