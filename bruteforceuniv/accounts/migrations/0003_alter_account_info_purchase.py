# Generated by Django 3.2.5 on 2021-09-06 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_auto_20210824_0101"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account_info",
            name="purchase",
            field=models.BooleanField(
                default=False, help_text="구매안내 어쩌고 저ㄱㅉ거 구매한 사람 체크 안했으면 가서 구매하기~"
            ),
        ),
    ]
