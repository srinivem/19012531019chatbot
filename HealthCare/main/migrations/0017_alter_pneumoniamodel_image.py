# Generated by Django 4.1.1 on 2022-10-03 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0016_alter_pneumoniamodel_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pneumoniamodel",
            name="image",
            field=models.ImageField(upload_to="File/disease/pneumonia/"),
        ),
    ]
