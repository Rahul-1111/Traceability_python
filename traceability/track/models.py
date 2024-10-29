from django.db import models

class TorqueData(models.Model):
    part_number = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    shift = models.CharField(max_length=50)

    # Station 1 fields
    station1_torque1 = models.IntegerField()
    station1_torque2 = models.IntegerField()
    station1_torque3 = models.IntegerField()
    station1_status = models.CharField(max_length=2)

    # Station 2 fields
    station2_torque1 = models.IntegerField()
    station2_torque2 = models.IntegerField()
    station2_torque3 = models.IntegerField()
    station2_status = models.CharField(max_length=2)

    # Station 3 fields
    station3_torque1 = models.IntegerField()
    station3_torque2 = models.IntegerField()
    station3_torque3 = models.IntegerField()
    station3_status = models.CharField(max_length=2)

    # Station 4 fields
    station4_torque1 = models.IntegerField()
    station4_torque2 = models.IntegerField()
    station4_torque3 = models.IntegerField()
    station4_status = models.CharField(max_length=2)
