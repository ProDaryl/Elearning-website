# Generated by Django 5.1 on 2024-08-30 14:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0004_rename_room_name_message_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatroom.room'),
        ),
    ]