# Generated by Django 4.2.5 on 2024-03-21 04:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0071_alter_advertisment_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 21, 4, 1, 46, 623199, tzinfo=datetime.timezone.utc)),
        ),
    ]
