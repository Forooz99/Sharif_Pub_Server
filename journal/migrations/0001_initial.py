# Generated by Django 4.2 on 2024-01-31 12:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Journal",
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
                ("name", models.CharField(max_length=50, unique=True)),
                ("logo", models.ImageField(null=True, upload_to="journal_logos/")),
                ("creationDate", models.DateTimeField(null=True)),
                ("department_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Volume",
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
                ("number", models.IntegerField()),
                ("title", models.CharField(max_length=300)),
                ("description", models.TextField()),
                ("releaseDate", models.DateTimeField(auto_now_add=True)),
                ("img", models.ImageField(null=True, upload_to="volume_images/")),
                (
                    "file",
                    models.FileField(
                        null=True,
                        upload_to="volume_files/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions="pdf"
                            )
                        ],
                    ),
                ),
                (
                    "journal",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="journal.journal",
                    ),
                ),
            ],
        ),
    ]