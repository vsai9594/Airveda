from django.shortcuts import get_object_or_404,get_list_or_404

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView

from  rest_framework import status
from webapp.models import Devices,TemperatureReading,HumidityReading
from webapp.serializers import ReadingSerializer,getTempdata,getHumiditydata
from rest_framework.response import Response

class DeviceCreate(CreateAPIView):
    serializer_class = ReadingSerializer
    queryset = Devices.objects.all()
    def get(self, request):
        reading = Devices.objects.all()
        serializer = ReadingSerializer(reading, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=ReadingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        reading = Devices.objects.all()
        serializer_reading = ReadingSerializer(reading, many=True)
        return Response(serializer_reading.data)

        return Response(serializer.data)


class deviceDelete(APIView):
    def get(self,request,my_id):
        device = get_object_or_404(Devices, uid=my_id)
        serializer = ReadingSerializer(device,many=False)
        return Response(serializer.data)
    def delete(self,request,my_id):
        device=get_object_or_404(Devices,uid=my_id)
        device.delete()
        return Response(status.HTTP_204_NO_CONTENT)


class readings(APIView):
    def get(self,request,my_id,property):
        start=self.request.GET['start_on']
        end=self.request.GET['end_on']
        if (property=="temperature" or property=="temp") :
            data=get_list_or_404(TemperatureReading,device_id=my_id,recorded_time__gte=start,recorded_time__lte=end)
            serializer_reading = getTempdata(data, many=True)
        elif property=="humidity":
            data=get_list_or_404(HumidityReading,device_id=my_id,recorded_time__gte=start,recorded_time__lte=end)
            serializer_reading = getHumiditydata(data, many=True)
        else:
            return Response("No details of : "+property)
        return Response(serializer_reading.data)

