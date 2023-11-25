from rest_framework import serializers
from .models import Complex , Company, Apartment, DirectAddress, District, PharentDistrict, City, ComplexImage

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city']

class PharentDistrictSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    city_id = serializers.PrimaryKeyRelatedField(
        queryset = City.objects.all(),
        source = 'city',
        write_only = True,
    )
    class Meta:
        model = PharentDistrict
        fields = ['city', 'pharentDistrict', 'city_id']

class DistrictSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    pharentDistrict = serializers.StringRelatedField()
    city_id = serializers.PrimaryKeyRelatedField(
        queryset = City.objects.all(),
        source = 'city',
        write_only = True,
    )
    pharentDistrict_id = serializers.PrimaryKeyRelatedField(
        queryset = PharentDistrict.objects.all(),
        source = 'pharentDistrict',
        write_only = True,
    )
    class Meta:
        model = District
        fields = ['city','pharentDistrict','district','city_id','pharentDistrict_id']

class DirectAddressSerializer(serializers.ModelSerializer):

    city = serializers.StringRelatedField()
    pharentDistrict = serializers.StringRelatedField()
    district = serializers.StringRelatedField()
    city_id = serializers.PrimaryKeyRelatedField(
        queryset = City.objects.all(),
        source = 'city',
        write_only = True,
    )
    pharentDistrict_id = serializers.PrimaryKeyRelatedField(
        queryset = PharentDistrict.objects.all(),
        source = 'pharentDistrict',
        write_only = True,
    )
    district_id = serializers.PrimaryKeyRelatedField(
        queryset = District.objects.all(),
        source = 'district',
        write_only = True,
    )
    
    class Meta:
        model = DirectAddress
        fields = ['id','city', 'pharentDistrict', 'district','street','city_id', 'pharentDistrict_id','district_id']
    
class ComplexImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplexImage
        fields='__all__'

class ComplexSerializer(serializers.ModelSerializer):
    address = DirectAddressSerializer()
    company = CompanySerializer()
    images = ComplexImageSerializer(many=True)
    class Meta:
        model = Complex
        fields = ['id','address','company','name','price_per_sq_meter','finished','space','number_of_apartments','number_of_houses','number_of_floors','phone_number','plot_area','type_of_roof', "images"]

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address_instance = DirectAddress.objects.create(**address_data)
        complex_instance = Complex.objects.create(address=address_instance, **validated_data)
        return complex_instance