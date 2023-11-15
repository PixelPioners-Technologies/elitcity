from rest_framework import viewsets 
from django_filters.rest_framework import DjangoFilterBackend
from .models import Complex , ComplexImage
from .serializers import ComplexSerializer , ComplexImageSerializer
from .filters import ComplexFilter
from rest_framework.filters import OrderingFilter

class ComplexViewSet(viewsets.ModelViewSet):
    queryset = Complex.objects.all()
    serializer_class = ComplexSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ComplexFilter

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['name', 'price_per_sq_meter', 'space']
    ordering = ['name']




class ComplexImageViewSet(viewsets.ModelViewSet):
    queryset = ComplexImage.objects.all()
    serializer_class = ComplexImageSerializer