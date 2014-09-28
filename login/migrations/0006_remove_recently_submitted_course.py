# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20140927_1942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recently_submitted',
            name='course',
        ),
    ]
