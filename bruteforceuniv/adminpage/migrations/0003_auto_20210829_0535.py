# Generated by Django 3.2.5 on 2021-08-29 05:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("adminpage", "0002_weeklyactivitypoints"),
    ]

    operations = [
        migrations.CreateModel(
            name="PointsStatus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("total_points", models.IntegerField(blank=True, default=0, null=True)),
                ("used_points", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="ActivityPoints",
        ),
    ]
