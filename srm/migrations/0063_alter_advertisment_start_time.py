# Generated by Django 4.2.5 on 2024-03-19 02:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0062_alter_advertisment_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 19, 2, 9, 35, 54303, tzinfo=datetime.timezone.utc)),
        ),
    ]
