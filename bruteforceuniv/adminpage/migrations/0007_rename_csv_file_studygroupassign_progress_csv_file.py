# Generated by Django 3.2.5 on 2021-09-23 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("adminpage", "0006_studygroupassign"),
    ]

    operations = [
        migrations.RenameField(
            model_name="studygroupassign",
            old_name="csv_file",
            new_name="progress_csv_file",
        ),
    ]
