# Generated by Django 3.2.6 on 2021-09-23 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210918_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='account_info',
            name='group',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
