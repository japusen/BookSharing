# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('edition', models.IntegerField()),
                ('dLink', models.URLField()),
                ('fileType', models.CharField(max_length=10, choices=[(b'pdf', b'pdf'), (b'epub', b'epub'), (b'djvu', b'djvu'), (b'torrent', b'torrent'), (b'other', b'other')])),
                ('upvotes', models.IntegerField()),
                ('downvotes', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('courseCode', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('courseTitle', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('deptName', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recently_Submitted',
            fields=[
                ('courseCode', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('courseTitle', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='course',
            name='dept',
            field=models.ForeignKey(to='content.Department'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='books',
            name='course',
            field=models.ForeignKey(to='content.Course'),
            preserve_default=True,
        ),
    ]
