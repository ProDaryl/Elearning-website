# Generated by Django 5.1.1 on 2024-09-09 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_enlistment', '0005_merge_20240908_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='duration',
        ),
    ]
