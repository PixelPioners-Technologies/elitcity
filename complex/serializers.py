from rest_framework import serializers
from .models import Complex

class ComplexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complex
        fields = '__all__'
