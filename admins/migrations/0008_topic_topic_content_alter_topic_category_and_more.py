# Generated by Django 4.2.5 on 2024-03-18 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_topiccontent_options_remove_topiccontent_name'),
        ('admins', '0007_remove_topic_added_by_remove_topic_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='topic_content',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_from_teacher', to='user.topiccontent'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.category'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.subject'),
        ),
    ]
