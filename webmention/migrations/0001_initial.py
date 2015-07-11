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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('response_body', models.TextField()),
                ('response_to', models.URLField()),
                ('source', models.URLField()),
                ('reviewed', models.BooleanField(default=False)),
                ('current', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'webmention',
                'verbose_name_plural': 'webmentions',
            },
        ),
    ]
