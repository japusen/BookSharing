# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20140927_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recently_submitted',
            name='courseTitle',
        ),
        migrations.RemoveField(
            model_name='recently_submitted',
            name='title',
        ),
        migrations.AddField(
            model_name='recently_submitted',
            name='book',
            field=models.ForeignKey(default='', to='login.Books'),
            preserve_default=False,
        ),
    ]
