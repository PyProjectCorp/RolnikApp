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
            name='Animals',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oznaczenie', models.CharField(max_length=100)),
                ('typ', models.CharField(default=b'KROWA', max_length=50, choices=[(b'KROWA', b'Krowa'), (b'SWINIA', b'Swinia'), (b'KURA', b'Kura'), (b'KACZKA', b'Kaczka'), (b'GES', b'Ges'), (b'INDYK', b'Indyk'), (b'INNE', b'Inne')])),
                ('old', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('price', models.IntegerField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
