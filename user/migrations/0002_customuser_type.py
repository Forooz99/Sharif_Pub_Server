# Generated by Django 4.2 on 2024-02-04 01:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="type",
            field=models.CharField(
                choices=[("READER", "reader"), ("PUBLISHER", "publisher")],
                default="READER",
                max_length=10,
            ),
        ),
    ]
