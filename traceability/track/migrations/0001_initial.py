# Generated by Django 5.1.2 on 2024-10-14 05:53

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TorqueData",
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
                ("part_number", models.CharField(max_length=100)),
                ("date", models.DateField()),
                ("time", models.TimeField()),
                ("shift", models.CharField(max_length=20)),
                ("station1_torque1", models.FloatField()),
                ("station1_torque2", models.FloatField()),
                ("station1_torque3", models.FloatField()),
                ("station1_status", models.CharField(max_length=2)),
                ("station2_torque1", models.FloatField()),
                ("station2_torque2", models.FloatField()),
                ("station2_torque3", models.FloatField()),
                ("station2_status", models.CharField(max_length=2)),
                ("station3_torque1", models.FloatField()),
                ("station3_torque2", models.FloatField()),
                ("station3_torque3", models.FloatField()),
                ("station3_status", models.CharField(max_length=2)),
                ("station4_torque1", models.FloatField()),
                ("station4_torque2", models.FloatField()),
                ("station4_torque3", models.FloatField()),
                ("station4_status", models.CharField(max_length=2)),
            ],
        ),
    ]
