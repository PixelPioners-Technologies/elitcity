from rest_framework import serializers
from .models import Complex , ComplexImage, Company, Apartment, GeoCities, GeoUbani, District, DirectAddress


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ComplexImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplexImage
        fields = ['complex', 'image']

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'

class DirectAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectAddress
        fields = '__all__'

class DistrictSerializer(serializers.ModelSerializer):
    street = DirectAddressSerializer(read_only=True)
    class Meta:
        model = District
        fields = '__all__'

class GeoUbaniSerializer(serializers.ModelSerializer):
    district = DistrictSerializer(read_only=True)
    class Meta:
        model = GeoUbani
        fields = '__all__'
class GeoCitiesSerializer(serializers.ModelSerializer):
    ubani = GeoUbaniSerializer(read_only=True)
    class Meta:
        model = GeoCities
        fields = '__all__'

class ComplexSerializer(serializers.ModelSerializer):
    images = ComplexImageSerializer(many=True, read_only=True)
    address = DirectAddressSerializer()
    class Meta:
        model = Complex
        fields = '__all__'