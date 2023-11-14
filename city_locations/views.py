from rest_framework import viewsets
from .serializers import CityLocationSerializer
from .models import CityLocations


class CityLocationViewSet(viewsets.ModelViewSet):
    queryset = CityLocations.objects.all()
    serializer_class = CityLocationSerializer