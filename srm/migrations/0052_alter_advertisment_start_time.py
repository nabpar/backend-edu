# Generated by Django 4.2.5 on 2024-03-15 20:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srm', '0051_alter_advertisment_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisment',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 15, 20, 1, 14, 436688, tzinfo=datetime.timezone.utc)),
        ),
    ]
