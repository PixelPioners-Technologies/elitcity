from rest_framework import serializers
from .models import Complex , ComplexImage, Company, Apartment , VIPComplex , TopCompany



class SecomdComplexImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplexImage
        fields = '__all__'



class ComplexImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplexImage
        fields = ['image']

    # Override the to_representation method to return only the image URL
    # ეს ფუნქცია აბრუნებინებს მხოლოდ სურატებს  ფიგურული ფრჩხილების გარეშე
    def to_representation(self, instance):
        return instance.image.url

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

    def get_images(self, obj):
        return list(obj.apartments.values_list('image', flat=True))


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



class TopCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = TopCompany
        fields = '__all__'
