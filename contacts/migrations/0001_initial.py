# Generated by Django 5.0.1 on 2024-02-04 19:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("first_name", models.CharField(max_length=64)),
                ("last_name", models.CharField(max_length=64)),
                ("phone_number", models.CharField(max_length=64)),
                ("email", models.EmailField(max_length=64)),
                (
                    "contact_type",
                    models.CharField(
                        choices=[("p", "Private"), ("b", "Business"), ("s", "School")],
                        max_length=4,
                    ),
                ),
                ("active", models.BooleanField(default=True)),
                ("created_at", models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
