from django.db import models

class Devices(models.Model):
    uid = models.CharField(max_length=20,unique=True)
    name=models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.name

class TemperatureReading(models.Model):
    temperature=models.CharField(max_length=20)
    recorded_time=models.CharField(max_length=100)
    device_id=models.CharField(max_length=20)


class HumidityReading(models.Model):
    humidity=models.CharField(max_length=20)
    recorded_time=models.CharField(max_length=100)
    device_id=models.CharField(max_length=20,null=True)



