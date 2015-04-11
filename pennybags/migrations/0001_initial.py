# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectedMarker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marker',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.CharField(max_length=1, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='marker',
            name='prize',
            field=models.ForeignKey(to='pennybags.Prize'),
        ),
        migrations.AddField(
            model_name='collectedmarker',
            name='marker',
            field=models.ForeignKey(to='pennybags.Marker'),
        ),
        migrations.AddField(
            model_name='collectedmarker',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
