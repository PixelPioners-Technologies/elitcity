from rest_framework import serializers
from .models import Complex , ComplexImage


class ComplexImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComplexImage
        fields = ['complex', 'image']





class ComplexSerializer(serializers.ModelSerializer):
    images = ComplexImageSerializer(many=True, read_only=True)
    class Meta:
        model = Complex
        fields = '__all__'
