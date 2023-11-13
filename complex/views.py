from rest_framework import viewsets
from .models import Complex
from .serializers import ComplexSerializer

class ComplexViewSet(viewsets.ModelViewSet):
    queryset = Complex.objects.all()
    serializer_class = ComplexSerializer
