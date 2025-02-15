# Generated by Django 5.1 on 2024-09-12 10:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Abc",
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
                ("name", models.CharField(max_length=50)),
                ("product", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=50)),
                ("address", models.EmailField(max_length=50)),
                ("phone", models.CharField(max_length=50)),
            ],
        ),
    ]
