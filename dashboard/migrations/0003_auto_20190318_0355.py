# Generated by Django 2.1.5 on 2019-03-18 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]