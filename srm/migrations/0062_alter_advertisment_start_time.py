# Generated by Django 4.2.5 on 2024-03-18 09:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0061_alter_advertisment_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 18, 9, 21, 10, 147024, tzinfo=datetime.timezone.utc)),
        ),
    ]