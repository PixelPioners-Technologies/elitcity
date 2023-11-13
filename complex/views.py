from rest_framework import viewsets 
from .models import Complex , ComplexImage
from .serializers import ComplexSerializer , ComplexImageSerializer


class ComplexViewSet(viewsets.ModelViewSet):
    queryset = Complex.objects.all()
    serializer_class = ComplexSerializer



class ComplexImageViewSet(viewsets.ModelViewSet):
    queryset = ComplexImage.objects.all()
    serializer_class = ComplexImageSerializer