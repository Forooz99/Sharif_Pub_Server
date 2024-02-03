# Generated by Django 4.2 on 2024-02-03 10:40

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
                    "name",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                (
                    "logo",
                    models.ImageField(
                        blank=True, null=True, upload_to="journal_logos/"
                    ),
                ),
                ("slogan", models.CharField(blank=True, max_length=150)),
                (
                    "director_name",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                (
                    "chief_editor",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                ("establishment_date", models.DateTimeField(blank=True, null=True)),
                (
                    "department_name",
                    models.CharField(
                        blank=True,
                        choices=[
                            (None, "Select a major"),
                            ("CE", "Computer Engineering"),
                            ("CS", "Computer Science"),
                            ("CVE", "Civil Engineering"),
                            ("EE", "Electrical Engineering"),
                            ("ME", "Mechanical Engineering"),
                            ("CME", "Chemical Engineering"),
                            ("AE", "Aerospace Engineering"),
                            ("PHY", "Physics"),
                            ("MATH", "Mathematics"),
                            ("CHEM", "Chemistry"),
                        ],
                        max_length=4,
                    ),
                ),
            ],
            options={
                "db_table": "Journal",
                "permissions": [],
            },
        ),
        migrations.CreateModel(
            name="Volume",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("number", models.IntegerField()),
                ("title", models.CharField(max_length=300)),
                ("description", models.TextField(blank=True)),
                ("release_date", models.DateTimeField(auto_now_add=True)),
                (
                    "cover_img",
                    models.ImageField(
                        blank=True, null=True, upload_to="volume_cover_images/"
                    ),
                ),
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
            options={
                "db_table": "Volume",
                "permissions": [],
            },
        ),
    ]
