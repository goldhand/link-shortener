# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_link_link_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='views',
            field=models.IntegerField(default=0, help_text=b'View Counter'),
        ),
    ]
