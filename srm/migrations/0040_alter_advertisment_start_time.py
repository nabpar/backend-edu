# Generated by Django 4.2.5 on 2024-03-14 05:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0039_alter_advertisment_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 14, 5, 42, 15, 47478, tzinfo=datetime.timezone.utc)),
        ),
    ]
