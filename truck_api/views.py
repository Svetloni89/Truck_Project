from rest_framework import generics

# Create your views here.
from truck_api.serializers import TruckSerializer
from truck_app.models import Truck


class TruckListApiView(generics.ListCreateAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer


class TruckDetailsApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Truck.objects.all()
    serializer_class = TruckSerializer
