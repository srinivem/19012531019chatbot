# Generated by Django 4.1.1 on 2022-10-02 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0010_registrationmodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="registrationmodel",
            name="confirm",
            field=models.CharField(default="", max_length=20),
        ),
    ]