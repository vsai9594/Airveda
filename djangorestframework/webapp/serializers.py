from rest_framework import serializers
from webapp.models import Devices,TemperatureReading,HumidityReading

class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Devices
        fields="__all__"

class getTempdata(serializers.ModelSerializer):
    class Meta:
        model = TemperatureReading
        fields = "__all__"

class getHumiditydata(serializers.ModelSerializer):
    class Meta:
        model=HumidityReading
        fields="__all__"