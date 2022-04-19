# Generated by Django 2.2.2 on 2019-07-11 10:21

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myquora', '0009_auto_20190702_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2019, 7, 11, 10, 21, 8, 18040, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2019, 7, 11, 10, 21, 8, 18068, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2019, 7, 11, 10, 21, 8, 16707, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2019, 7, 11, 10, 21, 8, 17427, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2019, 7, 11, 10, 21, 8, 17453, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2019, 7, 11, 10, 21, 8, 18667, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2019, 7, 11, 10, 21, 8, 18691, tzinfo=utc), null=True),
        ),
    ]
