# Generated by Django 4.2.5 on 2024-03-21 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_topiccontent_date_updated_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TopicContent',
        ),
    ]
