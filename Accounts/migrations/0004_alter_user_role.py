# Generated by Django 4.2.5 on 2024-03-14 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('STUDENT', 'Student'), ('TEACHER', 'Teacher'), ('ADMIN', 'Admin')], max_length=10),
        ),
    ]
