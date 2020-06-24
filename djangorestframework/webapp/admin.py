from django.contrib import admin

from webapp.models import Devices,TemperatureReading,HumidityReading
admin.site.register(Devices)
admin.site.register(TemperatureReading)
admin.site.register(HumidityReading)

