# Generated by Django 4.1.1 on 2022-09-30 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_alter_medicinemodel_definition_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="medicinemodel",
            name="definition",
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name="medicinemodel",
            name="effects",
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name="medicinemodel",
            name="prescription",
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name="medicinemodel",
            name="warnings",
            field=models.CharField(max_length=700),
        ),
    ]