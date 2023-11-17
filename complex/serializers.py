from rest_framework import serializers
from .models import Complex , ComplexImage, Company, Apartment




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
    apartments = ApartmentSerializer(many=True, read_only=True)
    class Meta:
        model = Complex
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    complex = ComplexSerializer(many=True, read_only=True)
    class Meta:
        model = Company
        fields = '__all__'