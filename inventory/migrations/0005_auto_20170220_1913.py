# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-20 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20170202_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='style',
            name='site',
            field=models.SmallIntegerField(choices=[(1, 'yt'), (2, 'bg')], default=1),
        ),
        migrations.AlterField(
            model_name='style',
            name='status',
            field=models.SmallIntegerField(choices=[(1, '정상'), (0, '승인 필요'), (-1, '삭제됨')], default=0),
        ),
    ]