# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20140925_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='courseLetter',
            field=models.CharField(default='', max_length=10, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='courseNo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseTitle',
            field=models.CharField(max_length=100),
        ),
    ]
