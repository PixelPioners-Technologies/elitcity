from rest_framework import viewsets , generics
from .models import Complex , ComplexImage, Company
from .serializers import ComplexSerializer , ComplexImageSerializer, CompanySerializer


class ComplexViewSet(viewsets.ModelViewSet):
    queryset = Complex.objects.all()
    serializer_class = ComplexSerializer



class ComplexImageViewSet(viewsets.ModelViewSet):
    queryset = ComplexImage.objects.all()
    serializer_class = ComplexImageSerializer


''' კომპანიის ცხრილის შექმნა, ზოგიერთი ველის შეყვანას აუცილებელი ველები არ აქვს
ანუ დამრეგისტრირებელს შეუძლია ის ინფორმაცია მიაწოდოს რაც აწყობს
'''
class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


''' კომპანიის ცხრილის ამოღება ( ჩვენება )... სავარაუდოდ ფრონტს გამოადგება'''
class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer