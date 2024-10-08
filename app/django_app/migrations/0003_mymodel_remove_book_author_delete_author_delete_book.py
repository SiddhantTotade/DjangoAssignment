# Generated by Django 5.1.1 on 2024-10-08 08:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("django_app", "0002_author_book"),
    ]

    operations = [
        migrations.CreateModel(
            name="MyModel",
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
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name="book",
            name="author",
        ),
        migrations.DeleteModel(
            name="Author",
        ),
        migrations.DeleteModel(
            name="Book",
        ),
    ]
