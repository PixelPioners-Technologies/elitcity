from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
#from .filters import ComplexFilter, ApartmentFilter
from rest_framework.pagination import LimitOffsetPagination

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100



class CityViewset(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    pagination_class = CustomLimitOffsetPagination
    
class LanguageViewset(viewsets.ModelViewSet):
    queryset = Lang.objects.prefetch_related('cities').all()
    serializer_class = LangSerializer
    pagination_class = CustomLimitOffsetPagination

# class PharentDistrictViewset(viewsets.ModelViewSet):
#     queryset = PharentDistrict.objects.all()
#     serializer_class = PharentDistrictSerializer
#     pagination_class = CustomLimitOffsetPagination

# class DistrictViewset(viewsets.ModelViewSet):
#     queryset = District.objects.all()
#     serializer_class = DistrictSerializer
#     pagination_class = CustomLimitOffsetPagination

# class DirectAddressViewset(viewsets.ModelViewSet):
#     queryset = DirectAddress.objects.all()
#     serializer_class = DirectAddressSerializerForView
#     pagination_class = CustomLimitOffsetPagination


# class ComplexViewSet(viewsets.ModelViewSet):
#     queryset = Complex.objects.all()
#     serializer_class = ComplexSerializer
#     filter_backends = [DjangoFilterBackend]
#     # Assuming you will create ComplexFilter
#     filterset_class = ComplexFilter
#     pagination_class = CustomLimitOffsetPagination

# class ApartmentViewSet(viewsets.ModelViewSet):
#     queryset = Apartment.objects.all()
#     serializer_class = ApartmentSerializer
#     filter_backends = [DjangoFilterBackend]
#     # Assuming you will create ApartmentFilter
#     filterset_class = ApartmentFilter
#     pagination_class = CustomLimitOffsetPagination

# class CompanyViewSet(viewsets.ModelViewSet):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializerForView
#     pagination_class = CustomLimitOffsetPagination

# class ComplexImageViewSet(viewsets.ModelViewSet):
#     queryset = ComplexImage.objects.all()
#     serializer_class = ComplexImageSerializerForView
#     pagination_class = CustomLimitOffsetPagination

# class ApartmentImageViewSet(viewsets.ModelViewSet):
#     queryset = ApartmentImage.objects.all()
#     serializer_class = ApartmentImageSerializer
#     pagination_class = CustomLimitOffsetPagination
