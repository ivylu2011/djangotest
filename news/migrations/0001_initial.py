# Generated by Django 4.2 on 2023-04-20 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NewsUnit",
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
                ("catego", models.CharField(max_length=10)),
                ("nickname", models.CharField(max_length=20)),
                ("title", models.CharField(max_length=50)),
                ("message", models.TextField()),
                ("pubtime", models.DateTimeField(auto_now=True)),
                ("enabled", models.BooleanField(default=False)),
                ("press", models.IntegerField(default=0)),
            ],
        ),
    ]
