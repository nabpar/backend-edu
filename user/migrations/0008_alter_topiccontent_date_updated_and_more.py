# Generated by Django 4.2.5 on 2024-03-21 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_topiccontent_status_alter_topiccontent_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topiccontent',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='topiccontent',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'DRAFT'), ('REVIEW', 'REVIEW'), ('REJECTED', 'REJECTED'), ('PUBLISHED', 'PUBLISHED')], default='DRAFT', max_length=15),
        ),
    ]
