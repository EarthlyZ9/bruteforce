# Generated by Django 3.2.5 on 2021-09-01 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("discussions", "0004_comment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="question",
        ),
    ]
