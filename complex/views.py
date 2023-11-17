from rest_framework import viewsets
from .models import Complex , ComplexImage, Company, Apartment
from .serializers import ComplexSerializer , ComplexImageSerializer, CompanySerializer, ApartmentSerializer

from rest_framework.pagination import LimitOffsetPagination

''' Pagination class '''
class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class ComplexViewSet(viewsets.ModelViewSet):
    queryset = Complex.objects.all()
    serializer_class = ComplexSerializer
    pagination_class = CustomLimitOffsetPagination



class ComplexImageViewSet(viewsets.ModelViewSet):
    queryset = ComplexImage.objects.all()
    serializer_class = ComplexImageSerializer
    pagination_class = CustomLimitOffsetPagination


''' კომპანიის ცხრილის შექმნა, ზოგიერთი ველის შეყვანას აუცილებელი ველები არ აქვს
ანუ დამრეგისტრირებელს შეუძლია ის ინფორმაცია მიაწოდოს რაც აწყობს
'''

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = CustomLimitOffsetPagination


class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    pagination_class = CustomLimitOffsetPagination