# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import links.models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='link_key',
            field=models.SlugField(default=links.models.set_link_key,
                                   help_text=b'Custom shortend version of link',
                                   unique=True, max_length=100),
        ),
    ]
