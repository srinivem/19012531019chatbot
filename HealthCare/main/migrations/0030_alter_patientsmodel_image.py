# Generated by Django 4.1.1 on 2022-10-26 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0029_alter_patientsmodel_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patientsmodel",
            name="image",
            field=models.FileField(upload_to="images/"),
        ),
    ]
