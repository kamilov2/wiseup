# Generated by Django 4.2.11 on 2024-05-08 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_book_book"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="description",
        ),
        migrations.RemoveField(
            model_name="subcategory",
            name="description",
        ),
    ]