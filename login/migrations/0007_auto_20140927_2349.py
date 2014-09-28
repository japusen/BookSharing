# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_remove_recently_submitted_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='downvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='books',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recently_submitted',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
