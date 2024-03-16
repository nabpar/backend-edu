# Generated by Django 4.2.5 on 2024-03-15 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0004_topic_subtopic'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='subtopic',
        ),
        migrations.CreateModel(
            name='TopicContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('topic', models.TextField()),
                ('content', models.TextField()),
                ('file_upload', models.FileField(blank=True, null=True, upload_to=user.models.TopicFiles)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.category')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.subject')),
                ('teacher_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name', 'date_created', 'date_updated'],
                'abstract': False,
            },
        ),
    ]