# Generated by Django 3.2.5 on 2021-08-26 04:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("activities", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="htmlfruits",
            name="voter",
            field=models.ManyToManyField(
                related_name="voter_htmlfruits", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="htmlfruits",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="author_htmlfruits",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
