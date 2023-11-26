from rest_framework import serializers
from .models import Complex , Company, Apartment, \
    DirectAddress, District, PharentDistrict, City, \
    ComplexImage, VIPComplex, TopCompany, ApartmentImage

class CompanySerializerForView(serializers.ModelSerializer):
    complexes = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = '__all__'

    def get_complexes(self, obj):
        return list(obj.complexes.values_list('id', flat=True))

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
        fields = ['city', 
                  'pharentDistrict', 
                  'city_id']

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
        fields = ['city',
                  'pharentDistrict',
                  'district',
                  'city_id',
                  'pharentDistrict_id']

class DirectAddressSerializerForView(serializers.ModelSerializer):

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
        fields = ['id',
                  'city', 
                  'pharentDistrict', 
                  'district',
                  'street',
                  'latitude', 
                  'longitude',
                  'city_id', 
                  'pharentDistrict_id',
                  'district_id']

class DirectAddressSerializer(serializers.ModelSerializer):

    city = serializers.StringRelatedField()
    pharentDistrict = serializers.StringRelatedField()
    district = serializers.StringRelatedField()
    class Meta:
        model = DirectAddress
        fields = ['id',
                  'city', 
                  'pharentDistrict', 
                  'district',
                  'street',
                  'latitude', 
                  'longitude']

class ComplexImageSerializerForView(serializers.ModelSerializer):
    class Meta:
        model = ComplexImage
        fields = ['complex', 
                  'images']

class ComplexImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplexImage
        fields = ['images']
    def to_representation(self, instance):
        return instance.images.url

class ApartmentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentImage
        fields = ['apartment', 
                  'images']        

class ComplexSerializer(serializers.ModelSerializer):
    # address = DirectAddressSerializer(read_only=True)
    company = CompanySerializer(read_only=True)
    images = ComplexImageSerializer(many=True, read_only=True)
    address = serializers.PrimaryKeyRelatedField(
        queryset=DirectAddress.objects.all(),
        write_only=True
    )
    company = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(),
        write_only=True
    )

    class Meta:
        model = Complex
        fields = ['id', 
                  'company', 
                  'address',
                  'name',
                  'price_per_sq_meter', 
                  'finished', 'space', 
                  'number_of_apartments', 
                  'number_of_houses', 
                  'number_of_floors', 
                  'phone_number', 
                  'plot_area', 
                  'type_of_roof', 
                  'images']
        
    def create(self, validated_data):
        address_data = validated_data.pop('address')
        # direct_address_instance = DirectAddress.objects.create(**address_data)
        complex_instance = Complex.objects.create(address=address_data, **validated_data)
        return complex_instance
    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Include the 'address' field in the response
        data['address'] = DirectAddressSerializer(instance.address).data
        data['company'] = CompanySerializer(instance.company).data
        return data
    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     # Include the 'address' field in the response
        
    #     return data

class VIPComplexSerializer(serializers.ModelSerializer):
    class Meta:
        model = VIPComplex
        fields = '__all__'

class TopCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = TopCompany
        fields = '__all__'