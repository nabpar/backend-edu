# Generated by Django 4.2.5 on 2024-03-21 04:01

import admins.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0012_topic_assign_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('file_upload', models.FileField(blank=True, null=True, upload_to=admins.models.TopicFiles)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('DRAFT', 'DRAFT'), ('REVIEW', 'REVIEW'), ('REJECTED', 'REJECTED'), ('PUBLISHED', 'PUBLISHED')], default='DRAFT', max_length=15)),
                ('status_message', models.CharField(blank=True, max_length=255, null=True)),
                ('topic', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='content', to='admins.topic')),
            ],
        ),
    ]