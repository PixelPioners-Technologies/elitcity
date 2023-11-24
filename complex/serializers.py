from rest_framework import serializers
from .models import Complex , ComplexImage, Company, Apartment , VIPComplex



class ComplexImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplexImage
        fields = ['complex', 'image']

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'


class ComplexSerializer(serializers.ModelSerializer):
    images = ComplexImageSerializer(many=True, read_only=True)
    apartments = serializers.SerializerMethodField()
    class Meta:
        model = Complex
        fields = '__all__'

    def get_apartments(self, obj):
        return list(obj.apartments.values_list('id', flat=True))



class CompanySerializer(serializers.ModelSerializer):
    complexes = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = '__all__'

    def get_complexes(self, obj):
        return list(obj.complexes.values_list('id', flat=True))


class VIPComplexSerializer(serializers.ModelSerializer):
    class Meta:
        model = VIPComplex
        fields = '__all__'





