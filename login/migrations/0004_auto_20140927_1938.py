# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20140925_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recently_submitted',
            name='courseCode',
        ),
        migrations.AddField(
            model_name='recently_submitted',
            name='course',
            field=models.ForeignKey(default='', to='login.Course'),
            preserve_default=False,
        ),
    ]
