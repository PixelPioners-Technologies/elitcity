from django.db import models

class Language(models.Model):
    language = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.language
'''
-----------------------------------------------------------------------
            CITY MODELS
-----------------------------------------------------------------------
'''     
class City_KA(models.Model):
    city_ka = models.CharField(max_length=50, unique=True)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return self.city_ka
    
class City_EN(models.Model):
    city_en = models.CharField(max_length=50, unique=True)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return self.city_en

class City_RU(models.Model):
    city_ru = models.CharField(max_length=50, unique=True)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return self.city_ru
'''
-----------------------------------------------------------------------
            PHERENTDISTRICT MODELS
-----------------------------------------------------------------------
''' 
class PharentDistrict_KA(models.Model):
    city_ka = models.ForeignKey(City_KA, on_delete=models.CASCADE)
    pharentDistrict_ka = models.CharField(max_length=50, unique=True)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return self.pharentDistrict_ka
    

class PharentDistrict_EN(models.Model):
    city_en = models.ForeignKey(City_EN, on_delete=models.CASCADE)
    pharentDistrict_en = models.CharField(max_length=50, unique=True)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return self.pharentDistrict_en
    
class PharentDistrict_RU(models.Model):
    city_ru = models.ForeignKey(City_RU, on_delete=models.CASCADE)
    pharentDistrict_ru = models.CharField(max_length=50, unique=True)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return self.pharentDistrict_ru 
'''
-----------------------------------------------------------------------
            DISTRICT MODELS
-----------------------------------------------------------------------
''' 
class District_KA(models.Model):
    city_ka = models.ForeignKey(City_KA, on_delete=models.CASCADE)
    pharentDistrict_ka = models.ForeignKey(PharentDistrict_KA, on_delete=models.CASCADE)
    district_ka = models.CharField(max_length=50, unique=True)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return self.district_ka

class District_EN(models.Model):
    city_en = models.ForeignKey(City_EN, on_delete=models.CASCADE)
    pharentDistrict_en = models.ForeignKey(PharentDistrict_EN, on_delete=models.CASCADE)
    district_en = models.CharField(max_length=50, unique=True)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return self.district_en
    
class District_RU(models.Model):
    city_ru = models.ForeignKey(City_RU, on_delete=models.CASCADE)
    pharentDistrict_ru = models.ForeignKey(PharentDistrict_RU, on_delete=models.CASCADE)
    district_ru = models.CharField(max_length=50, unique=True)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return self.district_ru
'''
-----------------------------------------------------------------------
            STREET_NAME MODELS
-----------------------------------------------------------------------
''' 
class Street_Name_KA(models.Model):
    city_ka = models.ForeignKey(City_KA, on_delete=models.CASCADE)
    pharentDistrict_ka = models.ForeignKey(PharentDistrict_KA, on_delete=models.CASCADE)
    district_ka = models.ForeignKey(District_KA, on_delete=models.CASCADE)
    street_name_ka = models.CharField(max_length=50)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return self.street_name_ka

class Street_Name_EN(models.Model):
    city_en = models.ForeignKey(City_EN, on_delete=models.CASCADE)
    pharentDistrict_en = models.ForeignKey(PharentDistrict_KA, on_delete=models.CASCADE)
    district_ka = models.ForeignKey(District_KA, on_delete=models.CASCADE)
    street_name_en = models.CharField(max_length=50)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return self.street_name_en
    
class Street_Name_RU(models.Model):
    city_ru = models.ForeignKey(City_RU, on_delete=models.CASCADE)
    pharentDistrict_ru = models.ForeignKey(PharentDistrict_KA, on_delete=models.CASCADE)
    district_ka = models.ForeignKey(District_KA, on_delete=models.CASCADE)
    street_name_ru = models.CharField(max_length=50)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return self.street_name_ru
'''
-----------------------------------------------------------------------
            ADDRESS MODELS
-----------------------------------------------------------------------
''' 
class Address_KA(models.Model):
    city_ka = models.ForeignKey(City_KA, on_delete=models.CASCADE)
    pharentDistrict_ka = models.ForeignKey(PharentDistrict_KA, on_delete=models.CASCADE)
    district_ka = models.ForeignKey(District_KA, on_delete=models.CASCADE)
    street_name_ka = models.ForeignKey(Street_Name_KA, on_delete=models.CASCADE)
    address_ka = models.CharField(max_length=30)
    longitude = models.FloatField()
    latitude = models.FloatField()
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return f"{self.city_ka.city_ka} - {self.pharentDistrict_ka.pharentDistrict_ka} - {self.district_ka.district_ka} - {self.street_name_ka.street_name_ka} - {self.address_ka}"

class Address_EN(models.Model):
    city_en = models.ForeignKey(City_EN, on_delete=models.CASCADE)
    pharentDistrict_en = models.ForeignKey(PharentDistrict_EN, on_delete=models.CASCADE)
    district_en = models.ForeignKey(District_EN, on_delete=models.CASCADE)
    street_name_en = models.ForeignKey(Street_Name_EN, on_delete=models.CASCADE)
    address_en = models.CharField(max_length=30)
    longitude = models.FloatField()
    latitude = models.FloatField()
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return f"{self.city_en.city_en} - {self.pharentDistrict_en.pharentDistrict_en} - {self.district_en.district_en} - {self.street_name_en.street_name_en} - {self.address_en}"
    
class Address_RU(models.Model):
    city_ru = models.ForeignKey(City_RU, on_delete=models.CASCADE)
    pharentDistrict_ru = models.ForeignKey(PharentDistrict_RU, on_delete=models.CASCADE)
    district_ru = models.ForeignKey(District_RU, on_delete=models.CASCADE)
    street_name_ru = models.ForeignKey(Street_Name_RU, on_delete=models.CASCADE)
    address_ru = models.CharField(max_length=30)
    longitude = models.FloatField()
    latitude = models.FloatField()
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return f"{self.city_ru.city_ru} - {self.pharentDistrict_ru.pharentDistrict_ru} - {self.district_ru.district_ru} - {self.street_name_ru.street_name_ru} - {self.address_ru}"
'''
-----------------------------------------------------------------------
            COMPANY MODELS
-----------------------------------------------------------------------
''' 
class Company_Names(models.Model):
    internal_name = models.CharField(max_length=255)
    Mobile = models.CharField(max_length=20)
    Mobile_Home = models.CharField(max_length=20)
    email = models.EmailField()
    companyweb = models.URLField(max_length=200, blank=True, null=True)
    facebook_page = models.URLField(blank=True, null=True)
    visibility =models.BooleanField(default=True)
    def __str__(self):
        return self.internal_name
    
class Company_Images(models.Model):
    internal_name = models.ForeignKey(Company_Names, on_delete=models.CASCADE)
    logocompany = models.ImageField(upload_to='company_logos/', blank=True, null=True, unique=True)
    background_image = models.ImageField(upload_to='company_background_images/', blank=True, null=True, unique=True)
    def __str__(self):
        return self.internal_name.internal_name

class Company_KA(models.Model):
    internal_name = models.ForeignKey(Company_Images, on_delete=models.CASCADE)
    name_ka = models.CharField(max_length=255)
    address_ka = models.TextField()
    aboutcompany_ka = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name_ka

class Company_EN(models.Model):
    internal_name = models.ForeignKey(Company_Images, on_delete=models.CASCADE)
    name_en = models.CharField(max_length=255)
    address_en = models.TextField()
    aboutcompany_en = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name_en
    
class Company_RU(models.Model):
    internal_name = models.ForeignKey(Company_Images, on_delete=models.CASCADE)
    name_ru = models.CharField(max_length=255)
    address_ru = models.TextField()
    aboutcompany_ru = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name_ru
'''
-----------------------------------------------------------------------
            COMPLEX MODELS
-----------------------------------------------------------------------
''' 
class Complex_Names(models.Model):
    internal_complex_name = models.CharField(max_length=255, unique=True)
    price_per_sq_meter = models.DecimalField(max_digits=10, decimal_places=2)
    finished = models.BooleanField()
    vipComplex = models.BooleanField()
    visibiliti = models.BooleanField(default=True)
    space = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_apartments = models.IntegerField()
    number_of_houses = models.IntegerField()
    number_of_floors = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    plot_area = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.internal_complex_name
    
class Complex_Images(models.Model):
    complex = models.ForeignKey(Complex_Names, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='complex_images/', unique=True)
    def __str__(self):
        return self.complex.internal_complex_name
    
class Complex_KA(models.Model):
    internal_complex_name = models.ForeignKey(Complex_Images, on_delete=models.CASCADE)
    complex_name_ka = models.CharField(max_length=200, unique=True)
    company_ka = models.ForeignKey(Company_KA, on_delete=models.CASCADE)
    address_ka = models.ForeignKey(Address_KA, on_delete=models.CASCADE)
    type_of_roof_ka = models.CharField(max_length=100)
    
    def __str__(self):
        return self.internal_complex_name.complex.internal_complex_name
    
class Complex_EN(models.Model):
    internal_complex_name = models.ForeignKey(Complex_Images, on_delete=models.CASCADE)
    complex_name_en = models.CharField(max_length=200, unique=True)
    company_en = models.ForeignKey(Company_EN, on_delete=models.CASCADE)
    address_en = models.ForeignKey(Address_EN, on_delete=models.CASCADE)
    type_of_roof_en = models.CharField(max_length=100)
    
    def __str__(self):
        return self.internal_complex_name.complex.internal_complex_name
    
class Complex_RU(models.Model):
    internal_complex_name = models.ForeignKey(Complex_Images, on_delete=models.CASCADE)
    complex_name_ru = models.CharField(max_length=200, unique=True)
    company_ru = models.ForeignKey(Company_RU, on_delete=models.CASCADE)
    address_ru = models.ForeignKey(Address_RU, on_delete=models.CASCADE)
    type_of_roof_ru = models.CharField(max_length=100)
    
    def __str__(self):
        return self.internal_complex_name.complex.internal_complex_name