# Generated by Django 4.2.5 on 2024-03-21 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0012_topic_assign_to'),
        ('user', '0006_remove_topiccontent_teacher_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='topiccontent',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'DRAFT'), ('REVIEW', 'REVIEW'), ('APPROVED', 'APPROVED'), ('REJECTED', 'REJECTED'), ('PUBLISHED', 'PUBLISHED')], default='DRAFT', max_length=15),
        ),
        migrations.AlterField(
            model_name='topiccontent',
            name='topic',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='content', to='admins.topic'),
        ),
    ]
