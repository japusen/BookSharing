# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('umail', models.EmailField(max_length=75, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=15)),
                ('username', models.CharField(unique=True, max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
