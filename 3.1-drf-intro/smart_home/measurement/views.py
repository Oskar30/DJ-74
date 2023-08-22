from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, CreateAPIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

class TempViewList(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    
class OneSensorVieweUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class AddMeasurements(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
