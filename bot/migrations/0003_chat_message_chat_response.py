# Generated by Django 4.2.2 on 2023-06-19 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_rename_user_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='message',
            field=models.TextField(default='no message'),
        ),
        migrations.AddField(
            model_name='chat',
            name='response',
            field=models.TextField(default='no response'),
        ),
    ]
