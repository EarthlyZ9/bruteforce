# Generated by Django 3.2.5 on 2021-09-24 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adminpage", "0007_rename_csv_file_studygroupassign_progress_csv_file"),
    ]

    operations = [
        migrations.RenameField(
            model_name="progresspointsfile",
            old_name="file",
            new_name="progress_csv_file",
        ),
        migrations.RenameField(
            model_name="studygroupassign",
            old_name="progress_csv_file",
            new_name="file",
        ),
        migrations.RemoveField(
            model_name="progresspointsfile",
            name="period",
        ),
        migrations.RemoveField(
            model_name="studygroupassign",
            name="season",
        ),
        migrations.AddField(
            model_name="progresspointsfile",
            name="season",
            field=models.IntegerField(default=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="studygroupassign",
            name="period",
            field=models.CharField(
                choices=[
                    ("1", "1차 진도율"),
                    ("2", "2차 진도율"),
                    ("3", "3차 진도율"),
                    ("final", "최종 진도율"),
                    ("completion", "종료 시점 진도율 (수료증)"),
                ],
                default=1,
                max_length=20,
            ),
            preserve_default=False,
        ),
    ]