# Generated by Django 4.2.11 on 2024-05-08 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="book",
            field=models.FileField(default=0, upload_to="books/"),
            preserve_default=False,
        ),
    ]
