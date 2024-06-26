# Generated by Django 4.2.5 on 2024-03-20 03:28

from django.db import migrations, models
from django.utils import timezone

class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_topiccontent_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topiccontent',
            name='teacher_name',
        ),
        migrations.AddField(
            model_name='topiccontent',
            name='status_message',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='topiccontent',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=timezone.now()),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topiccontent',
            name='date_updated',
            field=models.DateTimeField(auto_now_add=True, default=timezone.now()),
            preserve_default=False,
        ),
    ]
