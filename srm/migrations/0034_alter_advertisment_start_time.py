# Generated by Django 4.2.5 on 2024-03-07 05:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0033_alter_advertisment_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 7, 5, 42, 17, 211626, tzinfo=datetime.timezone.utc)),
        ),
    ]
