# Generated by Django 3.2.5 on 2021-09-18 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpage', '0004_progresspointsfile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='progresspointsfile',
            old_name='title',
            new_name='period',
        ),
    ]
