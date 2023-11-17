from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Complex, Apartment, Company, ComplexImage
from .serializers import ComplexSerializer, ApartmentSerializer, CompanySerializer, ComplexImageSerializer
from .filters import ComplexFilter, ApartmentFilter
from rest_framework.pagination import LimitOffsetPagination

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

class ComplexViewSet(viewsets.ModelViewSet):
    queryset = Complex.objects.all()
    serializer_class = ComplexSerializer
    filter_backends = [DjangoFilterBackend]
    # Assuming you will create ComplexFilter
    filterset_class = ComplexFilter
    pagination_class = CustomLimitOffsetPagination

class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    filter_backends = [DjangoFilterBackend]
    # Assuming you will create ApartmentFilter
    filterset_class = ApartmentFilter
    pagination_class = CustomLimitOffsetPagination

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = CustomLimitOffsetPagination

class ComplexImageViewSet(viewsets.ModelViewSet):
    queryset = ComplexImage.objects.all()
    serializer_class = ComplexImageSerializer
    pagination_class = CustomLimitOffsetPagination
