# Generated by Django 2.2 on 2021-09-17 10:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20210914_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_gm_steps',
            name='filter_id',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='过滤id'),
        ),
        migrations.AlterField(
            model_name='db_notice',
            name='ctime',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 17, 10, 14, 5, 888927, tzinfo=utc), verbose_name='保存日期'),
        ),
    ]
