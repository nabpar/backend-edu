# Generated by Django 4.2.5 on 2024-01-05 14:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0007_alter_advertisment_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 5, 14, 18, 52, 750102, tzinfo=datetime.timezone.utc)),
        ),
    ]
