# Generated by Django 3.0.2 on 2020-03-04 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pmanager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platform',
            name='slug',
        ),
    ]
