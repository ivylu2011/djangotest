# Generated by Django 4.1.7 on 2023-03-09 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="student",
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
                ("stdName", models.CharField(max_length=50)),
                ("stdID", models.CharField(max_length=10)),
                ("stdSex", models.CharField(default="M", max_length=2)),
                ("stdBirth", models.DateField()),
                ("stdEmail", models.EmailField(blank=True, default="", max_length=100)),
                ("stdPhone", models.CharField(blank=True, default="", max_length=20)),
                (
                    "stdAddress",
                    models.CharField(blank=True, default="", max_length=255),
                ),
            ],
        ),
    ]
