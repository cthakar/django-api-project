# Generated by Django 3.2.3 on 2021-05-23 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scratchapi', '0002_user_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='userid',
        ),
    ]
