# Generated by Django 4.2.11 on 2024-05-08 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_remove_profile_description_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="password",
        ),
        migrations.AlterField(
            model_name="profile",
            name="email",
            field=models.CharField(max_length=100),
        ),
    ]
