# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebMentionResponse',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('response_body', models.TextField()),
                ('response_to', models.URLField()),
                ('source', models.URLField()),
                ('reviewed', models.BooleanField(default=False)),
                ('current', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
