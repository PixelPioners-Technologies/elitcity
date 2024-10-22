from rest_framework import serializers
from .models import *
from .utils import S3Helper


class LangSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = ['language']
'''
-----------------------------------------------------------------------
            CITY SERIALIZERS
-----------------------------------------------------------------------
'''
class City_KA_Serializer(serializers.ModelSerializer):
    lang_id = serializers.PrimaryKeyRelatedField(
        queryset = Language.objects.all(),
        source = 'lang',
        many = True,
        write_only = True,
    )
    lang = LangSerializer(many=True, read_only=True)
    class Meta:
        model = City_KA
        fields = ['id','city_ka','lang','lang_id']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {'id': data['id'],
                'city_ka': data['city_ka'],
                'language': data['lang'][0]['language']}

class City_EN_Serializer(serializers.ModelSerializer):
    lang_id = serializers.PrimaryKeyRelatedField(
        queryset = Language.objects.all(),
        source = 'lang',
        many = True,
        write_only = True,
    )
    lang = LangSerializer(many=True, read_only=True)
    class Meta:
        model = City_EN
        fields = ['id','city_en','lang','lang_id']
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {'id': data['id'],
                'city_en': data['city_en'],
                'language': data['lang'][0]['language']}
        
class City_RU_Serializer(serializers.ModelSerializer):
    lang_id = serializers.PrimaryKeyRelatedField(
        queryset = Language.objects.all(),
        source = 'lang',
        many = True,
        write_only = True,
    )
    lang = LangSerializer(many=True, read_only=True)
    class Meta:
        model = City_RU
        fields = ['id','city_ru','lang','lang_id']
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {'id': data['id'],
                'city_ru': data['city_ru'],
                'language': data['lang'][0]['language']}
'''
-----------------------------------------------------------------------
            PHARENTDISTRICT SERIALIZERS
-----------------------------------------------------------------------
'''
class PharentDistrict_KA_Serializer(serializers.ModelSerializer):
    lang_id = serializers.PrimaryKeyRelatedField(
        queryset = Language.objects.all(),
        source = 'lang',
        many = True,
        write_only = True,
    )
    city_id = serializers.PrimaryKeyRelatedField(
        queryset = City_KA.objects.all(),
        source = 'city_ka',
        write_only = True,
    )
    city_ka = City_KA_Serializer( read_only=True)
    class Meta:
        model = PharentDistrict_KA
        fields = ['id','city_id','city_ka', 'pharentDistrict_ka', 'lang_id']
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            'id':data['id'],
            'city_ka': data['city_ka']['city_ka'],
            'pharentDistrict_ka': data['pharentDistrict_ka'],
            'language': data['city_ka']['language'],
        }

class PharentDistrict_EN_Serializer(serializers.ModelSerializer):
    lang_id = serializers.PrimaryKeyRelatedField(
        queryset = Language.objects.all(),
        source = 'lang',
        many = True,
        write_only = True,
    )
    city_id = serializers.PrimaryKeyRelatedField(
        queryset = City_EN.objects.all(),
        source = 'city_en',
        write_only = True,
    )
    city_en = City_EN_Serializer(read_only=True)
    class Meta:
        model = PharentDistrict_EN
        fields = ['id','city_id','city_en', 'pharentDistrict_en', 'lang_id']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            'id':data['id'],
            'city_en': data['city_en']['city_en'],
            'pharentDistrict_en': data['pharentDistrict_en'],
            'language': data['city_en']['language'],
        }

class PharentDistrict_RU_Serializer(serializers.ModelSerializer):
    lang_id = serializers.PrimaryKeyRelatedField(
        queryset = Language.objects.all(),
        source = 'lang',
        many = True,
        write_only = True,
    )
    city_id = serializers.PrimaryKeyRelatedField(
        queryset = City_RU.objects.all(),
        source = 'city_ru',
        write_only = True,
    )
    city_ru = City_RU_Serializer(read_only=True)
    class Meta:
        model = PharentDistrict_RU
        fields = ['id','city_id','city_ru', 'pharentDistrict_ru', 'lang_id']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            'id':data['id'],
            'city_ru': data['city_ru']['city_ru'],
            'pharentDistrict_ru': data['pharentDistrict_ru'],
            'language': data['city_ru']['language'],
        }
'''
-----------------------------------------------------------------------
            DISTRICT SERIALIZERS
-----------------------------------------------------------------------
'''
class District_KA_Serializer(serializers.ModelSerializer):
    lang_id = serializers.PrimaryKeyRelatedField(
        queryset = Language.objects.all(),
        source = 'lang',
        many = True,
        write_only = True,
    )
    city_id = serializers.PrimaryKeyRelatedField(
        queryset = City_KA.objects.all(),
        source = 'city_ka',
        write_only = True,
    )
    pharentDistrict_ka_id = serializers.PrimaryKeyRelatedField(
        queryset = PharentDistrict_KA.objects.all(),
        source = 'pharentDistrict_ka',
        write_only = True,
    )
    pharentDistrict_ka = PharentDistrict_KA_Serializer(read_only=True)
    class Meta:
        model = District_KA
        fields = ['id', 'city_id','pharentDistrict_ka_id', 'pharentDistrict_ka', 'district_ka', 'lang_id']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            'id': data['id'],
            'city_ka': data['pharentDistrict_ka']['city_ka'],
            'pharentDistrict_ka': data['pharentDistrict_ka']['pharentDistrict_ka'],
            'district_ka': data['district_ka'],
            'language': data['pharentDistrict_ka']["language"],
            
        }

class District_EN_Serializer(serializers.ModelSerializer):
    lang_id = serializers.PrimaryKeyRelatedField(
        queryset = Language.objects.all(),
        source = 'lang',
        many = True,
        write_only = True,
    )
    city_id = serializers.PrimaryKeyRelatedField(
        queryset = City_EN.objects.all(),
        source = 'city_en',
        write_only = True,
    )
    pharentDistrict_en_id = serializers.PrimaryKeyRelatedField(
        queryset = PharentDistrict_EN.objects.all(),
        source = 'pharentDistrict_en',
        write_only = True,
    )

    pharentDistrict_en = PharentDistrict_EN_Serializer(read_only=True)
    class Meta:
        model = District_EN
        fields = ['id', 'city_id','pharentDistrict_en_id', 'pharentDistrict_en', 'district_en', 'lang_id']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            'id': representation['id'],
            'city_en': representation['pharentDistrict_en']['city_en'],
            'pharentDistrict_en': representation['pharentDistrict_en']['pharentDistrict_en'],
            'district_en': representation['district_en'],
            'language': representation['pharentDistrict_en']['language'],
        }

class District_RU_Serializer(serializers.ModelSerializer):
    lang_id = serializers.PrimaryKeyRelatedField(
        queryset = Language.objects.all(),
        source = 'lang',
        many = True,
        write_only = True,
    )
    city_id = serializers.PrimaryKeyRelatedField(
        queryset = City_RU.objects.all(),
        source = 'city_ru',
        write_only = True,
    )
    pharentDistrict_ru_id = serializers.PrimaryKeyRelatedField(
        queryset = PharentDistrict_RU.objects.all(),
        source = 'pharentDistrict_ru',
        write_only = True,
    )
    pharentDistrict_ru = PharentDistrict_RU_Serializer(read_only=True)
    class Meta:
        model = District_RU
        fields = ['id', 'city_id', 'pharentDistrict_ru_id','pharentDistrict_ru', 'district_ru', 'lang_id']
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            'id': representation['id'],
            'lang': representation['pharentDistrict_ru']["language"],
            'city_ru': representation['pharentDistrict_ru']['city_ru'],
            'pharentDistrict_ru': representation['pharentDistrict_ru']['pharentDistrict_ru'],
            'district_ru': representation['district_ru'],
            'lang': representation['pharentDistrict_ru']['language'],
        }
'''
-----------------------------------------------------------------------
            STREETNAME SERIALIZERS
-----------------------------------------------------------------------
'''
class Street_Name_KA_Serializer(serializers.ModelSerializer):
    lang_id = serializers.PrimaryKeyRelatedField(
        queryset = Language.objects.all(),
        source = 'lang',
        many = True,
        write_only = True,
    )
    city_id = serializers.PrimaryKeyRelatedField(
        queryset = City_KA.objects.all(),
        source = 'city_ka',
        write_only = True,
    )
    district_id = serializers.PrimaryKeyRelatedField(
        queryset = District_KA.objects.all(),
        source = 'district_ka',
        write_only = True,
    )
    district_ka = District_KA_Serializer(read_only=True)
    class Meta:
        model = Street_Name_KA
        fields = ['id',"city_id", 'pharentDistrict_ka', 'district_id','district_ka', 'street_name_ka', "lang_id"]
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            'id': representation['id'],
            'lang': representation['district_ka']['language'],
            'city_ka': representation['district_ka']['city_ka'],
            'pharentDistrict_ka': representation['district_ka']['pharentDistrict_ka'],
            'district_ka': representation['district_ka']['district_ka'],
            'street_name_ka':representation['street_name_ka'],
        }

class Street_Name_EN_Serializer(serializers.ModelSerializer):
    lang_id = serializers.PrimaryKeyRelatedField(
        queryset = Language.objects.all(),
        source = 'lang',
        many = True,
        write_only = True,
    )
    city_id = serializers.PrimaryKeyRelatedField(
        queryset = City_EN.objects.all(),
        source = 'city_en',
        write_only = True,
    )
    district_id = serializers.PrimaryKeyRelatedField(
        queryset = District_EN.objects.all(),
        source = 'district_en',
        write_only = True,
    )
    district_en = District_EN_Serializer(read_only=True)
    class Meta:
        model = Street_Name_EN
        fields = ['id',"city_id", 'pharentDistrict_en', "district_id",'district_en', 'street_name_en', "lang_id"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            'id': representation['id'],
            'lang': representation['district_en']['language'],
            'city_en': representation['district_en']['city_en'],
            'pharentDistrict_en': representation['district_en']['pharentDistrict_en'],
            'district_en': representation['district_en']['district_en'],
            'street_name_en':representation['street_name_en'],
        }

class Street_Name_RU_Serializer(serializers.ModelSerializer):
    lang_id = serializers.PrimaryKeyRelatedField(
        queryset = Language.objects.all(),
        source = 'lang',
        many = True,
        write_only = True,
    )
    city_id = serializers.PrimaryKeyRelatedField(
        queryset = City_RU.objects.all(),
        source = 'city_ru',
        write_only = True,
    )
    district_id = serializers.PrimaryKeyRelatedField(
        queryset = District_RU.objects.all(),
        source = 'district_ru',
        write_only = True,
    )
    district_ru = District_RU_Serializer(read_only=True)
    class Meta:
        model = Street_Name_RU
        fields = ['id',"city_id", 'pharentDistrict_ru', 'district_id','district_ru', 'street_name_ru', "lang_id"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            'id': data['id'],
            'lang': data['district_ru']['lang'],
            'city_ru': data['district_ru']['city_ru'],
            'pharentDistrict_ru': data['district_ru']['pharentDistrict_ru'],
            'district_ru': data['district_ru']['district_ru'],
            'street_name_ru':data['street_name_ru'],
        }

'''
-----------------------------------------------------------------------
            ADDRESS SERIALIZERS
-----------------------------------------------------------------------
'''

class Address_KA_Serializer(serializers.ModelSerializer):
    lang_id = serializers.PrimaryKeyRelatedField(
        queryset = Language.objects.all(),
        source = 'lang',
        many = True,
        write_only = True,
    )
    city_id = serializers.PrimaryKeyRelatedField(
        queryset = City_KA.objects.all(),
        source = 'city_ka',
        write_only = True,
    )
    district_id = serializers.PrimaryKeyRelatedField(
        queryset = District_KA.objects.all(),
        source = 'district_ka',
        write_only = True,
    )
    street_name_ka_id = serializers.PrimaryKeyRelatedField(
        queryset = Street_Name_KA.objects.all(),
        source = 'street_name_ka',
        write_only = True,
    )
    street_name_ka = Street_Name_KA_Serializer(read_only=True)
    class Meta:
        model = Address_KA
        fields = ['city_id','pharentDistrict_ka','district_id','street_name_ka_id','id', 'street_name_ka',"address_ka", "longitude", "latitude",'lang_id']
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            'id': data['id'],
            'lang': data['street_name_ka']['lang'],
            'city_ka': data['street_name_ka']['city_ka'],
            'pharentDistrict_ka': data['street_name_ka']['pharentDistrict_ka'],
            'district_ka': data['street_name_ka']['district_ka'],
            'street_name_ka':data['street_name_ka']['street_name_ka'],
            'address_ka':data['address_ka'],
            'longitude': data['longitude'],
            'latitude': data['latitude'],
        }

class Address_EN_Serializer(serializers.ModelSerializer):
    lang_id = serializers.PrimaryKeyRelatedField(
        queryset = Language.objects.all(),
        source = 'lang',
        many = True,
        write_only = True,
    )
    city_id = serializers.PrimaryKeyRelatedField(
        queryset = City_EN.objects.all(),
        source = 'city_en',
        write_only = True,
    )
    district_id = serializers.PrimaryKeyRelatedField(
        queryset = District_EN.objects.all(),
        source = 'district_en',
        write_only = True,
    )
    street_name_en_id = serializers.PrimaryKeyRelatedField(
        queryset = Street_Name_EN.objects.all(),
        source = 'street_name_en',
        write_only = True,
    )
    street_name_en = Street_Name_EN_Serializer(read_only=True)
    class Meta:
        model = Address_EN
        fields = ['city_id','pharentDistrict_en','district_id','street_name_en_id','id', 'street_name_en',"address_en", "longitude", "latitude",'lang_id']
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            'id': data['id'],
            'lang': data['street_name_en']['lang'],
            'city_en': data['street_name_en']['city_en'],
            'pharentDistrict_en': data['street_name_en']['pharentDistrict_en'],
            'district_en': data['street_name_en']['district_en'],
            'street_name_en':data['street_name_en']['street_name_en'],
            'address_en':data['address_en'],
            'longitude': data['longitude'],
            'latitude': data['latitude'],
        }

class Address_RU_Serializer(serializers.ModelSerializer):
    lang_id = serializers.PrimaryKeyRelatedField(
        queryset = Language.objects.all(),
        source = 'lang',
        many = True,
        write_only = True,
    )
    city_id = serializers.PrimaryKeyRelatedField(
        queryset = City_RU.objects.all(),
        source = 'city_ru',
        write_only = True,
    )
    district_id = serializers.PrimaryKeyRelatedField(
        queryset = District_RU.objects.all(),
        source = 'district_ru',
        write_only = True,
    )
    street_name_ru_id = serializers.PrimaryKeyRelatedField(
        queryset = Street_Name_RU.objects.all(),
        source = 'street_name_ru',
        write_only = True,
    )
    street_name_ru = Street_Name_RU_Serializer(read_only=True)
    class Meta:
        model = Address_RU
        fields = ['city_id','pharentDistrict_ru','district_id','street_name_ru_id','id', 'street_name_ru',"address_ru", "longitude", "latitude",'lang_id']
    def to_representation(self, instance):
        data = super().to_representation(instance)

        return {
            'id': data['id'],
            'lang': data['street_name_ru']['lang'],
            'city_ru': data['street_name_ru']['city_ru'],
            'pharentDistrict_ru': data['street_name_ru']['pharentDistrict_ru'],
            'district_ru': data['street_name_ru']['district_ru'],
            'street_name_ru':data['street_name_ru']['street_name_ru'],
            'address_ru':data['address_ru'],
            'longitude': data['longitude'],
            'latitude': data['latitude'],
        }
    
'''
-----------------------------------------------------------------------
            COMAPNY SERIALIZERS
-----------------------------------------------------------------------
'''

class Company_name_serializers(serializers.ModelSerializer):

    class Meta:
        model = Company_Names
        fields = '__all__'
    
    
class Company_Image_serializers(serializers.ModelSerializer):
    internal_name_id = serializers.PrimaryKeyRelatedField(
        queryset = Company_Names.objects.all(),
        source = 'internal_name',
        write_only = True
    )
    internal_name = Company_name_serializers(read_only = True)
    class Meta:
        model = Company_Images
        fields = ['id',"internal_name_id",'internal_name','logocompany','background_image']
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            'id':data['id'],
            'record_id':data['internal_name']['id'],
            'internal_name':data['internal_name']['internal_name'],
            'Mobile':data['internal_name']['Mobile'],
            'Mobile_Home':data['internal_name']['Mobile_Home'],
            'email':data['internal_name']['email'],
            'companyweb':data['internal_name']['companyweb'],
            'facebook_page':data['internal_name']['facebook_page'],
            'topCompany':data['internal_name']['topCompany'],
            'visibility':data['internal_name']['visibility'],
            'logocompany':data['logocompany'],
            'background_image':data['background_image'],
        }

class Company_KA_serializers(serializers.ModelSerializer):
    internal_name_id = serializers.PrimaryKeyRelatedField(
        queryset = Company_Images.objects.all(),
        source = 'internal_name',
        write_only = True,
    )
    internal_name = Company_Image_serializers(read_only=True)
    # topCompany_id = serializers.PrimaryKeyRelatedField(
    #     queryset = Company_Names.objects.all(),
    #     write_only = True,
    # )
    class Meta:
        model = Company_KA
        fields = ['id','internal_name_id', "internal_name", 'name_ka', 'address_ka', 'aboutcompany_ka']
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            'id':data['id'],
            'record_id':data['internal_name']['id'],
            'internal_name':data['internal_name']['internal_name'],
            'Mobile':data['internal_name']['Mobile'],
            'Mobile_Home':data['internal_name']['Mobile_Home'],
            'email':data['internal_name']['email'],
            'companyweb':data['internal_name']['companyweb'],
            'facebook_page':data['internal_name']['facebook_page'],
            'logocompany':data['internal_name']['logocompany'],
            'background_image':data['internal_name']['background_image'],
            'topCompany':data['internal_name']['topCompany'],
            'visibility':data['internal_name']['visibility'],
            'name_ka': data['name_ka'],
            'address_ka':data['address_ka'],
            'aboutcompany_ka':data['aboutcompany_ka'],
        }

class Company_EN_serializers(serializers.ModelSerializer):
    internal_name_id = serializers.PrimaryKeyRelatedField(
        queryset = Company_Images.objects.all(),
        source = 'internal_name',
        write_only = True,
    )
    internal_name = Company_Image_serializers(read_only=True)
    class Meta:
        model = Company_EN
        fields = ['id','internal_name_id', "internal_name", 'name_en', 'address_en', 'aboutcompany_en']
    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        return {
            'id':data['id'],
            'record_id':data['internal_name']['id'],
            'internal_name':data['internal_name']['internal_name'],
            'Mobile':data['internal_name']['Mobile'],
            'Mobile_Home':data['internal_name']['Mobile_Home'],
            'email':data['internal_name']['email'],
            'companyweb':data['internal_name']['companyweb'],
            'facebook_page':data['internal_name']['facebook_page'],
            'logocompany':data['internal_name']['logocompany'],
            'background_image':data['internal_name']['background_image'],
            'topCompany':data['internal_name']['topCompany'],
            'visibility':data['internal_name']['visibility'],
            'name_en': data['name_en'],
            'address_en':data['address_en'],
            'aboutcompany_en':data['aboutcompany_en'],
        }

class Company_RU_serializers(serializers.ModelSerializer):
    internal_name_id = serializers.PrimaryKeyRelatedField(
        queryset = Company_Images.objects.all(),
        source = 'internal_name',
        write_only = True,
    )
    internal_name = Company_Image_serializers(read_only=True)
    class Meta:
        model = Company_RU
        fields = ['id','internal_name_id', "internal_name", 'name_ru', 'address_ru', 'aboutcompany_ru']
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            'id':data['id'],
            'record_id':data['internal_name']['id'],
            'internal_name':data['internal_name']['internal_name'],
            'Mobile':data['internal_name']['Mobile'],
            'Mobile_Home':data['internal_name']['Mobile_Home'],
            'email':data['internal_name']['email'],
            'companyweb':data['internal_name']['companyweb'],
            'facebook_page':data['internal_name']['facebook_page'],
            'logocompany':data['internal_name']['logocompany'],
            'background_image':data['internal_name']['background_image'],
            'topCompany':data['internal_name']['topCompany'],
            'name_ru': data['name_ru'],
            'address_ru':data['address_ru'],
            'aboutcompany_ru':data['aboutcompany_ru'],
        }

'''
-----------------------------------------------------------------------
            COMPLEX SERIALIZERS
-----------------------------------------------------------------------
'''
class Complex_Name_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Complex_Names
        fields = '__all__'
    
class Complex_Image_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Complex_Images
        fields = ['internal_complex_name','images']

class Complex_KA_Serializers(serializers.ModelSerializer):    
    image_urls = serializers.SerializerMethodField()
    address_ka = Address_KA_Serializer(read_only = True)
    address_ka_id = serializers.PrimaryKeyRelatedField(
        queryset = Address_KA.objects.all(),
        source = "address_ka",
        write_only = True,
    )
    company_ka = Company_KA_serializers(read_only = True)
    company_ka_id = serializers.PrimaryKeyRelatedField(
        queryset = Company_KA.objects.all(),
        source = "company_ka",
        write_only = True,
    )
    complex_images_id = serializers.PrimaryKeyRelatedField(
        queryset = Complex_Images.objects.all(),
        source = 'complex_images',
        write_only = True
    )
    internal_complex_name = Complex_Name_Serializers(read_only=True)
    internal_complex_name_id = serializers.PrimaryKeyRelatedField(
        queryset = Complex_Names.objects.all(),
        source = 'internal_complex_name',
        write_only = True
    )
    class Meta:
        model = Complex_KA
        fields = [
            'id',
            'complex_name_ka',
            'internal_complex_name',
            'type_of_roof_ka',
            'image_urls',
            'company_ka',
            'address_ka',
            'complex_images_id',
            'internal_complex_name_id',
            'company_ka_id',
            'address_ka_id',
            'construction_type_ka',
            'submission_type_ka',
            'protection_type_ka',
            "description_ka", 
            ]
        
    def get_image_urls(self, instance):
        images = Complex_Images.objects.filter(internal_complex_name=instance.internal_complex_name)
        return [S3Helper.generate_signed_url(str(image.images)) for image in images]
    
class Complex_EN_Serializers(serializers.ModelSerializer):
    image_urls = serializers.SerializerMethodField()
    address_en = Address_EN_Serializer(read_only = True)
    address_en_id = serializers.PrimaryKeyRelatedField(
        queryset = Address_EN.objects.all(),
        source = "address_en",
        write_only = True,
    )
    company_en = Company_EN_serializers(read_only = True)
    company_en_id = serializers.PrimaryKeyRelatedField(
        queryset = Company_EN.objects.all(),
        source = "company_en",
        write_only = True,
    )
    complex_images_id = serializers.PrimaryKeyRelatedField(
        queryset = Complex_Images.objects.all(),
        source = 'complex_images',
        write_only = True
    )
    internal_complex_name = Complex_Name_Serializers(read_only=True)
    internal_complex_name_id = serializers.PrimaryKeyRelatedField(
        queryset = Complex_Names.objects.all(),
        source = 'internal_complex_name',
        write_only = True
    )
    class Meta:
        model = Complex_EN
        fields = [
            'id',
            'complex_name_en',
            'internal_complex_name',
            'type_of_roof_en',
            'image_urls',
            'company_en',
            'address_en',
            'complex_images_id',
            'internal_complex_name_id',
            'company_en_id',
            'address_en_id',
            'construction_type_en',
            'submission_type_en',
            'protection_type_en',
            "description_en", 
 
            ]
    def get_image_urls(self, instance):
        images = Complex_Images.objects.filter(internal_complex_name=instance.internal_complex_name)
        return [S3Helper.generate_signed_url(str(image.images)) for image in images]
    
class Complex_RU_Serializers(serializers.ModelSerializer):
    image_urls = serializers.SerializerMethodField()
    address_ru = Address_RU_Serializer(read_only = True)
    address_ru_id = serializers.PrimaryKeyRelatedField(
        queryset = Address_RU.objects.all(),
        source = "address_ru",
        write_only = True,
    )
    company_ru = Company_RU_serializers(read_only = True)
    company_ru_id = serializers.PrimaryKeyRelatedField(
        queryset = Company_RU.objects.all(),
        source = "company_ru",
        write_only = True,
    )
    complex_images_id = serializers.PrimaryKeyRelatedField(
        queryset = Complex_Images.objects.all(),
        source = 'complex_images',
        write_only = True
    )
    internal_complex_name = Complex_Name_Serializers(read_only=True)
    internal_complex_name_id = serializers.PrimaryKeyRelatedField(
        queryset = Complex_Names.objects.all(),
        source = 'internal_complex_name',
        write_only = True
    )
    class Meta:
        model = Complex_RU
        fields = [
            'id',
            'complex_name_ru',
            'internal_complex_name',
            'type_of_roof_ru',
            'image_urls',
            'company_ru',
            'address_ru',
            'complex_images_id',
            'internal_complex_name_id',
            'company_ru_id',
            'address_ru_id',
            'construction_type_ru',
            'submission_type_ru',
            'protection_type_ru',
            "description_ru", 

            ]
    def get_image_urls(self, instance):
        images = Complex_Images.objects.filter(internal_complex_name=instance.internal_complex_name)
        return [S3Helper.generate_signed_url(str(image.images)) for image in images]
    
'''
-----------------------------------------------------------------------
            APARTMENT SERIALIZERS
-----------------------------------------------------------------------
'''

class Appartment_Names_Serializer(serializers.ModelSerializer):
    complex = Complex_Name_Serializers(read_only = True)
    complex_id = serializers.PrimaryKeyRelatedField(
        queryset = Complex_Names.objects.all(),
        source = 'complex',
        write_only = True,
        required = False,
        allow_null=True,
    )
    class Meta:
        model = Appartment_Names
        fields = [
            'id',
            'created_at',
            'complex',
            'complex_id',
            'internal_apartment_name',
            'number_of_rooms', 
            'area',
            'full_price',
            'square_price',
            'floor_number',
            'is_available',
            'visibiliti',
            'metro',
            'Pharmacy',
            'supermarket',
            'square',
            'rooms',
            'kitchen',
            'Bathroom',
            'bedroom',
            'Balcony',
            'rank',
            'status'

            ]
# --------------------------------------------------------------------------
        # fEW
        # FWEFWEF
        # WEFWEF
class Appartment_Images_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Appartment_Images
        fields = '__all__'

class Appartment_KA_Serializer(serializers.ModelSerializer):
    internal_apartment_name = Appartment_Names_Serializer(read_only = True)
    internal_apartment_name_id = serializers.PrimaryKeyRelatedField(
        queryset = Appartment_Names.objects.all(),
        source = 'internal_apartment_name',
        write_only=True,
        
    )
    appartment_address_ka = Address_KA_Serializer(read_only = True)
    appartment_address_ka_id = serializers.PrimaryKeyRelatedField(
        queryset = Address_KA.objects.all(),
        source = 'appartment_address_ka',
        write_only=True
    )
    complex_ka = Complex_KA_Serializers(read_only=True)
    complex_ka_id = serializers.PrimaryKeyRelatedField(
        queryset = Complex_KA.objects.all(),
        source = 'complex_ka',
        write_only = True,
        required = False,
        allow_null=True,
    )
    appartment_images_id = serializers.PrimaryKeyRelatedField(
        queryset = Appartment_Images.objects.all(),
        source = 'appartment_images',
        write_only=True,
        
    )
    class Meta:
        model = Appartment_KA
        fields = [
            'id',
            'internal_apartment_name',
            'internal_apartment_name_id',
            'complex_ka',
            'complex_ka_id',
            'appartment_address_ka',
            'appartment_address_ka_id',
            'appartment_name_ka',
            'appartment_images_id',
            'test_field_ka'
            ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        image_urls = self.get_image_urls(instance)
        return {
            "id": data['id'],
            'complex_ka': data['complex_ka'],
            'internal_apartment_name' : {
                "id": data["internal_apartment_name"]['id'],
                "internal_apartment_name": data["internal_apartment_name"]["internal_apartment_name"],
                "number_of_rooms": data["internal_apartment_name"]['number_of_rooms'],
                "area": data["internal_apartment_name"]['area'],
                "full_price": data["internal_apartment_name"]['full_price'],
                'square_price' : data['internal_apartment_name']['square_price'],
                "floor_number": data["internal_apartment_name"]['floor_number'],
                "is_available": data["internal_apartment_name"]['is_available'],
                "visibiliti": data["internal_apartment_name"]['visibiliti'],

                "rooms": data["internal_apartment_name"]['rooms'],
                "kitchen": data["internal_apartment_name"]['kitchen'],
                "Bathroom": data["internal_apartment_name"]['Bathroom'],
                "bedroom": data["internal_apartment_name"]['bedroom'],
                "Balcony": data["internal_apartment_name"]['Balcony'],
                "rank": data["internal_apartment_name"]['rank'],
                "status": data["internal_apartment_name"]['status'],


            },
            'appartment_address_ka': data["appartment_address_ka"],
            'appartment_images': image_urls,
            'test_field_ka': data['test_field_ka'],
            'appartment_name_ka': data["appartment_name_ka"],


        }

    def get_image_urls(self, instance):
        images = Appartment_Images.objects.filter(internal_apartment_name=instance.internal_apartment_name)
        return [S3Helper.generate_signed_url(str(image.images)) for image in images]
    
class Appartment_EN_Serializer(serializers.ModelSerializer):
    internal_apartment_name = Appartment_Names_Serializer(read_only = True)
    internal_apartment_name_id = serializers.PrimaryKeyRelatedField(
        queryset = Appartment_Names.objects.all(),
        source = 'internal_apartment_name',
        write_only=True,
        
    )
    appartment_address_en = Address_EN_Serializer(read_only = True)
    appartment_address_en_id = serializers.PrimaryKeyRelatedField(
        queryset = Address_EN.objects.all(),
        source = 'appartment_address_en',
        write_only=True
    )
    complex_en = Complex_EN_Serializers(read_only=True)
    complex_en_id = serializers.PrimaryKeyRelatedField(
        queryset = Complex_EN.objects.all(),
        source = 'complex_en',
        write_only = True,
        required = False,
        allow_null=True,
    )
    appartment_images_id = serializers.PrimaryKeyRelatedField(
        queryset = Appartment_Images.objects.all(),
        source = 'appartment_images',
        write_only=True,
        
    )
    class Meta:
        model = Appartment_EN
        fields = [
            'id',
            'internal_apartment_name',
            'internal_apartment_name_id',
            'complex_en',
            'complex_en_id',
            'appartment_address_en',
            'appartment_address_en_id',
            'appartment_name_en',
            'appartment_images_id',
            'test_field_en'
            ]
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        image_urls = self.get_image_urls(instance)
        return {
            "id": data['id'],
            'complex_en': data['complex_en'],
            'internal_apartment_name' : {
                "id": data["internal_apartment_name"]['id'],
                "internal_apartment_name": data["internal_apartment_name"]["internal_apartment_name"],
                "number_of_rooms": data["internal_apartment_name"]['number_of_rooms'],
                "area": data["internal_apartment_name"]['area'],
                "full_price": data["internal_apartment_name"]['full_price'],
                'square_price' : data['internal_apartment_name']['square_price'],
                "floor_number": data["internal_apartment_name"]['floor_number'],
                "is_available": data["internal_apartment_name"]['is_available'],
                "visibiliti": data["internal_apartment_name"]['visibiliti'],
                "rooms": data["internal_apartment_name"]['rooms'],
                "kitchen": data["internal_apartment_name"]['kitchen'],
                "Bathroom": data["internal_apartment_name"]['Bathroom'],
                "bedroom": data["internal_apartment_name"]['bedroom'],
                "Balcony": data["internal_apartment_name"]['Balcony'],
                "rank": data["internal_apartment_name"]['rank'],
                "status": data["internal_apartment_name"]['status'],




            },
            'appartment_address_en': data["appartment_address_en"],
            'appartment_images': image_urls,
            'test_field_en': data['test_field_en'],
            'appartment_name_en': data["appartment_name_en"],
        }


    def get_image_urls(self, instance):
        images = Appartment_Images.objects.filter(internal_apartment_name=instance.internal_apartment_name)
        return [S3Helper.generate_signed_url(str(image.images)) for image in images]
    
class Appartment_RU_Serializer(serializers.ModelSerializer):
    internal_apartment_name = Appartment_Names_Serializer(read_only = True)
    internal_apartment_name_id = serializers.PrimaryKeyRelatedField(
        queryset = Appartment_Names.objects.all(),
        source = 'internal_apartment_name',
        write_only=True,
        
    )
    appartment_address_ru = Address_RU_Serializer(read_only = True)
    appartment_address_ru_id = serializers.PrimaryKeyRelatedField(
        queryset = Address_RU.objects.all(),
        source = 'appartment_address_ru',
        write_only=True
    )
    complex_ru = Complex_RU_Serializers(read_only=True)
    complex_ru_id = serializers.PrimaryKeyRelatedField(
        queryset = Complex_RU.objects.all(),
        source = 'complex_ru',
        write_only = True,
        required = False,
        allow_null=True,
    )
    appartment_images_id = serializers.PrimaryKeyRelatedField(
        queryset = Appartment_Images.objects.all(),
        source = 'appartment_images',
        write_only=True,
        
    )
    class Meta:
        model = Appartment_RU
        fields = [
            'id',
            'internal_apartment_name',
            'internal_apartment_name_id',
            'complex_ru',
            'complex_ru_id',
            'appartment_address_ru',
            'appartment_address_ru_id',
            'appartment_name_ru',
            'appartment_images_id',
            'test_field_ru'
            ]
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        image_urls = self.get_image_urls(instance)
        return {
            "id": data['id'],
            'complex_ru': data['complex_ru'],
            'internal_apartment_name' : {
                "id": data["internal_apartment_name"]['id'],
                "internal_apartment_name": data["internal_apartment_name"]["internal_apartment_name"],
                "number_of_rooms": data["internal_apartment_name"]['number_of_rooms'],
                "area": data["internal_apartment_name"]['area'],
                "full_price": data["internal_apartment_name"]['full_price'],
                'square_price' : data['internal_apartment_name']['square_price'],
                "floor_number": data["internal_apartment_name"]['floor_number'],
                "is_available": data["internal_apartment_name"]['is_available'],
                "visibiliti": data["internal_apartment_name"]['visibiliti'],
                "rooms": data["internal_apartment_name"]['rooms'],
                "kitchen": data["internal_apartment_name"]['kitchen'],
                "Bathroom": data["internal_apartment_name"]['Bathroom'],
                "bedroom": data["internal_apartment_name"]['bedroom'],
                "Balcony": data["internal_apartment_name"]['Balcony'],
                "rank": data["internal_apartment_name"]['rank'],
                "status": data["internal_apartment_name"]['status'],


            },
            'appartment_address_ru': data["appartment_address_ru"],
            'appartment_images': image_urls,
            'test_field_ru': data['test_field_ru'],
            'appartment_name_ru': data["appartment_name_ru"],


        }


    def get_image_urls(self, instance):
        images = Appartment_Images.objects.filter(internal_apartment_name=instance.internal_apartment_name)
        return [S3Helper.generate_signed_url(str(image.images)) for image in images]
    

'''
-----------------------------------------------------------------------
            MAP SERIALIZERS
-----------------------------------------------------------------------
'''
class District_KA_ForMap_Serializer(serializers.ModelSerializer):
    class Meta:
        model = District_KA
        fields = ['district_ka']

class PharentDistrict_KA_ForMap_Serializer(serializers.ModelSerializer):
    district_ka = District_KA_ForMap_Serializer(many=True, read_only=True)

    class Meta:
        model = PharentDistrict_KA
        fields = ['pharentDistrict_ka', 'district_ka']

class City_KA_ForMap_Serializer(serializers.ModelSerializer):
    pharentDistrict_ka = PharentDistrict_KA_ForMap_Serializer(many=True, read_only=True)

    class Meta:
        model = City_KA
        fields = ['city_ka', 'pharentDistrict_ka']


class District_EN_ForMap_Serializer(serializers.ModelSerializer):
    class Meta:
        model = District_EN
        fields = ['district_en']

class PharentDistrict_EN_ForMap_Serializer(serializers.ModelSerializer):
    district_en = District_EN_ForMap_Serializer(many=True, read_only=True)

    class Meta:
        model = PharentDistrict_EN
        fields = ['pharentDistrict_en', 'district_en']

class City_EN_ForMap_Serializer(serializers.ModelSerializer):
    pharentDistrict_en = PharentDistrict_EN_ForMap_Serializer(many=True, read_only=True)

    class Meta:
        model = City_EN
        fields = ['city_en', 'pharentDistrict_en']



class District_RU_ForMap_Serializer(serializers.ModelSerializer):
    class Meta:
        model = District_RU
        fields = ['district_ru']

class PharentDistrict_RU_ForMap_Serializer(serializers.ModelSerializer):
    district_ru = District_RU_ForMap_Serializer(many=True, read_only=True)

    class Meta:
        model = PharentDistrict_RU
        fields = ['pharentDistrict_ru', 'district_ru']

class City_RU_ForMap_Serializer(serializers.ModelSerializer):
    pharentDistrict_ru = PharentDistrict_RU_ForMap_Serializer(many=True, read_only=True)

    class Meta:
        model = City_RU
        fields = ['city_ru', 'pharentDistrict_ru']


'''
-----------------------------------------------------------------------
            PRIVATE APARTMENT SERIALIZERS
-----------------------------------------------------------------------
'''

class Private_Appartment_Images_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Private_Appartment_images
        fields = "__all__"

class Private_Appartment_Name_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Private_Appartment_Names
        fields = [
            "id",
            "internal_private_apartment_name",
            "number_of_rooms",
            "status",
            "area",
            'full_price',
            'square_price',
            'floor_number',
            'is_available',
            'visibiliti',
            'rank',
            'rooms',
            'kitchen',
            'Bathroom',
            'bedroom',
            'Balcony',
            "metro" ,
            "pharmacy" ,
            "supermarket" ,
            "square" ,


        ]


class Private_Appartment_EN_Serializer(serializers.ModelSerializer):
    internal_private_apartment_name = Private_Appartment_Name_Serializer(read_only = True)
    internal_private_apartment_name_id = serializers.PrimaryKeyRelatedField(
        queryset = Private_Appartment_Names.objects.all(),
        source = 'internal_private_apartment_name',
         write_only=True,
    ) 
    private_apartment_address_en = Address_EN_Serializer(read_only=True)
    private_apartment_address_en_id = serializers.PrimaryKeyRelatedField(
        queryset =  Address_EN.objects.all(),
        source = 'private_apartment_address_en',
    )
    private_apartment_images_id = serializers.PrimaryKeyRelatedField(
        queryset = Private_Appartment_images.objects.all(),
        source = 'private_apartment_images',
        write_only=True,
    )
    class Meta:
        model = Private_Appartment_EN
        fields = [
            'id',
            'internal_private_apartment_name',
            'internal_private_apartment_name_id',
            'private_apartment_address_en',
            'private_apartment_address_en_id',
            'private_apartment_name_en',
            'private_apartment_images_id',
            'about_en',

        ]
    def to_representation(self, instance):
        data = super().to_representation(instance)
        image_urls = self.get_image_urls(instance)
        return {
            "id": data['id'],
            'internal_private_apartment_name' : {
               "id": data["internal_private_apartment_name"]['id'],
                "internal_private_apartment_name": data["internal_private_apartment_name"]["internal_private_apartment_name"],
                "number_of_rooms": data["internal_private_apartment_name"]['number_of_rooms'],
                'status' : data["internal_private_apartment_name"]['status'] ,
                "area": data["internal_private_apartment_name"]['area'],
                "full_price": data["internal_private_apartment_name"]['full_price'],
                'square_price' : data['internal_private_apartment_name']['square_price'],
                "floor_number": data["internal_private_apartment_name"]['floor_number'],
                "is_available": data["internal_private_apartment_name"]['is_available'],
                "visibiliti": data["internal_private_apartment_name"]['visibiliti'],
                'rank':data['internal_private_apartment_name']['rank'],

                'rooms':data['internal_private_apartment_name']['rooms'],
                'kitchen':data['internal_private_apartment_name']['kitchen'],
                'Bathroom':data['internal_private_apartment_name']['Bathroom'],
                'bedroom':data['internal_private_apartment_name']['bedroom'],
                'Balcony':data['internal_private_apartment_name']['Balcony'],

                "metro" :data['internal_private_apartment_name']['metro'],
                "pharmacy" :data['internal_private_apartment_name']['pharmacy'],
                "supermarket" :data['internal_private_apartment_name']['supermarket'],
                "square" :data['internal_private_apartment_name']['square'],
                "metro" :data['internal_private_apartment_name']['metro'],
                "pharmacy" :data['internal_private_apartment_name']['pharmacy'],
                "supermarket" :data['internal_private_apartment_name']['supermarket'],
                "square" :data['internal_private_apartment_name']['square'],
            },
            'private_apartment_address_en': data["private_apartment_address_en"],
            'private_apartment_images': image_urls,
            'private_apartment_name_en': data['private_apartment_name_en'],
            'about_en': data['about_en'],

        }

    def get_image_urls(self, instance):
        images = Private_Appartment_images.objects.filter(internal_private_apartment_name=instance.internal_private_apartment_name)
        return [S3Helper.generate_signed_url(str(image.images)) for image in images]
    





class Private_Appartment_KA_Serializer(serializers.ModelSerializer):
    internal_private_apartment_name = Private_Appartment_Name_Serializer(read_only = True)
    internal_private_apartment_name_id = serializers.PrimaryKeyRelatedField(
        queryset = Private_Appartment_Names.objects.all(),
        source = 'internal_private_apartment_name',
         write_only=True,
    ) 
    private_apartment_address_ka = Address_KA_Serializer(read_only=True)
    private_apartment_address_ka_id = serializers.PrimaryKeyRelatedField(
        queryset =  Address_KA.objects.all(),
        source = 'private_apartment_address_ka',
    )
    private_apartment_images_id = serializers.PrimaryKeyRelatedField(
        queryset = Private_Appartment_images.objects.all(),
        source = 'private_apartment_images',
        write_only=True,
    )
    class Meta:
        model = Private_Appartment_KA
        fields = [
            'id',
            'internal_private_apartment_name',
            'internal_private_apartment_name_id',
            'private_apartment_address_ka',
            'private_apartment_address_ka_id',
            'private_apartment_name_ka',
            'private_apartment_images_id',
            'about_ka',

        ]
    def to_representation(self, instance):
        data = super().to_representation(instance)
        image_urls = self.get_image_urls(instance)
        print(data)
        return {
            "id": data['id'],
            'internal_private_apartment_name' : {
               "id": data["internal_private_apartment_name"]['id'],
                "internal_private_apartment_name": data["internal_private_apartment_name"]["internal_private_apartment_name"],
                "number_of_rooms": data["internal_private_apartment_name"]['number_of_rooms'],
                'status' : data["internal_private_apartment_name"]['status'] ,
                "area": data["internal_private_apartment_name"]['area'],
                "full_price": data["internal_private_apartment_name"]['full_price'],
                'square_price' : data['internal_private_apartment_name']['square_price'],
                "floor_number": data["internal_private_apartment_name"]['floor_number'],
                "is_available": data["internal_private_apartment_name"]['is_available'],
                "visibiliti": data["internal_private_apartment_name"]['visibiliti'],
                'rank':data['internal_private_apartment_name']['rank'],


                'rooms':data['internal_private_apartment_name']['rooms'],
                'kitchen':data['internal_private_apartment_name']['kitchen'],
                'Bathroom':data['internal_private_apartment_name']['Bathroom'],
                'bedroom':data['internal_private_apartment_name']['bedroom'],
                'Balcony':data['internal_private_apartment_name']['Balcony'],

                "metro" :data['internal_private_apartment_name']['metro'],
                "pharmacy" :data['internal_private_apartment_name']['pharmacy'],
                "supermarket" :data['internal_private_apartment_name']['supermarket'],
                "square" :data['internal_private_apartment_name']['square'],
                
            },
            'private_apartment_address_ka': data["private_apartment_address_ka"],
            'private_apartment_images': image_urls,
            'private_apartment_name_ka': data['private_apartment_name_ka'],
            'about_ka': data['about_ka'],

        }

    def get_image_urls(self, instance):
        images = Private_Appartment_images.objects.filter(internal_private_apartment_name=instance.internal_private_apartment_name)
        return [S3Helper.generate_signed_url(str(image.images)) for image in images]
    




class Private_Appartment_RU_Serializer(serializers.ModelSerializer):
    internal_private_apartment_name = Private_Appartment_Name_Serializer(read_only = True)
    internal_private_apartment_name_id = serializers.PrimaryKeyRelatedField(
        queryset = Private_Appartment_Names.objects.all(),
        source = 'internal_private_apartment_name',
         write_only=True,
    ) 
    private_apartment_address_ru = Address_RU_Serializer(read_only=True)
    private_apartment_address_ru_id = serializers.PrimaryKeyRelatedField(
        queryset =  Address_RU.objects.all(),
        source = 'private_apartment_address_ru',
    )
    private_apartment_images_id = serializers.PrimaryKeyRelatedField(
        queryset = Private_Appartment_images.objects.all(),
        source = 'private_apartment_images',
        write_only=True,
    )
    class Meta:
        model = Private_Appartment_RU
        fields = [
            'id',
            'internal_private_apartment_name',
            'internal_private_apartment_name_id',
            'private_apartment_address_ru',
            'private_apartment_address_ru_id',
            'private_apartment_name_ru',
            'private_apartment_images_id',
            'about_ru',
            

        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        image_urls = self.get_image_urls(instance)
        return {
            "id": data['id'],
            'internal_private_apartment_name' : {
               "id": data["internal_private_apartment_name"]['id'],
                "internal_private_apartment_name": data["internal_private_apartment_name"]["internal_private_apartment_name"],
                "number_of_rooms": data["internal_private_apartment_name"]['number_of_rooms'],
                'status' : data["internal_private_apartment_name"]['status'] ,
                "area": data["internal_private_apartment_name"]['area'],
                "full_price": data["internal_private_apartment_name"]['full_price'],
                'square_price' : data['internal_private_apartment_name']['square_price'],
                "floor_number": data["internal_private_apartment_name"]['floor_number'],
                "is_available": data["internal_private_apartment_name"]['is_available'],
                "visibiliti": data["internal_private_apartment_name"]['visibiliti'],
                'rank':data['internal_private_apartment_name']['rank'],


                'rooms':data['internal_private_apartment_name']['rooms'],
                'kitchen':data['internal_private_apartment_name']['kitchen'],
                'Bathroom':data['internal_private_apartment_name']['Bathroom'],
                'bedroom':data['internal_private_apartment_name']['bedroom'],
                'Balcony':data['internal_private_apartment_name']['Balcony'],

                "metro" :data['internal_private_apartment_name']['metro'],
                "pharmacy" :data['internal_private_apartment_name']['pharmacy'],
                "supermarket" :data['internal_private_apartment_name']['supermarket'],
                "square" :data['internal_private_apartment_name']['square'],
                

            },
            'private_apartment_address_ru': data["private_apartment_address_ru"],
            'private_apartment_images': image_urls,
            'private_apartment_name_ru': data['private_apartment_name_ru'],
            'about_ru': data['about_ru'],

        }

    def get_image_urls(self, instance):
        images = Private_Appartment_images.objects.filter(internal_private_apartment_name=instance.internal_private_apartment_name)
        return [S3Helper.generate_signed_url(str(image.images)) for image in images]
    
    
'''
-----------------------------------------------------------------------
            GROUND SERIALIZERS
-----------------------------------------------------------------------
'''

class Ground_Names_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ground_Names
        fields = [
            'id',
            'internal_ground_name',
            'area',
            'full_price',
            'square_price',
            'status',
            'rank',
            'phone_number',
            'is_available',
            'visibiliti',
            "about_land",
            ]

class Ground_Images_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ground_Images
        fields = '__all__'

class Ground_KA_Serializer(serializers.ModelSerializer):
    internal_ground_name = Ground_Names_Serializer(read_only = True)
    internal_ground_name_id = serializers.PrimaryKeyRelatedField(
        queryset = Ground_Names.objects.all(),
        source = 'internal_ground_name',
        write_only=True,
        required=False
    )
    ground_address_ka = Address_KA_Serializer(read_only = True)
    ground_address_ka_id = serializers.PrimaryKeyRelatedField(
        queryset = Address_KA.objects.all(),
        source = 'ground_address_ka',
        write_only=True,
        required=False
        
    )
    ground_images_id = serializers.PrimaryKeyRelatedField(
        queryset = Ground_Images.objects.all(),
        source = 'ground_images',
        write_only=True,
        required=False 
    )
    class Meta:
        model = Ground_KA
        fields = [
            'id',
            'internal_ground_name',
            'internal_ground_name_id',
            'ground_address_ka',
            'ground_address_ka_id',
            'ground_name_ka',
            'ground_images_id',
            ]
    def to_representation(self, instance):
        data = super().to_representation(instance)
        image_urls = self.get_image_urls(instance)
        return {
            "id": data['id'],
            'internal_ground_name' : {
                "id": data["internal_ground_name"]['id'],
                "internal_ground_name": data["internal_ground_name"]["internal_ground_name"],
                "area": data["internal_ground_name"]['area'],
                "full_price": data["internal_ground_name"]['full_price'],
                'square_price': data['internal_ground_name']['square_price'],
                'status':data['internal_ground_name']['status'],
                'rank':data['internal_ground_name']['rank'],
                'phone_number':data['internal_ground_name']['phone_number'],
                "is_available": data["internal_ground_name"]['is_available'],
                "visibiliti": data["internal_ground_name"]['visibiliti'],
                "about_land": data["internal_ground_name"]["about_land"],


            },
            'ground_address_ka': data["ground_address_ka"],
            'ground_name_ka':data['ground_name_ka'],
            'ground_images': image_urls,
        }


    def get_image_urls(self, instance):
        images = Ground_Images.objects.filter(internal_ground_name=instance.internal_ground_name)
        return [S3Helper.generate_signed_url(str(image.images)) for image in images]
      
class Ground_EN_Serializer(serializers.ModelSerializer):
    internal_ground_name = Ground_Names_Serializer(read_only = True)
    internal_ground_name_id = serializers.PrimaryKeyRelatedField(
        queryset = Ground_Names.objects.all(),
        source = 'internal_ground_name',
        write_only=True,
        required=False
        
    )
    ground_address_en = Address_EN_Serializer(read_only = True)
    ground_address_en_id = serializers.PrimaryKeyRelatedField(
        queryset = Address_EN.objects.all(),
        source = 'ground_address_en',
        write_only=True,
        required=False
    )
    ground_images_id = serializers.PrimaryKeyRelatedField(
        queryset = Ground_Images.objects.all(),
        source = 'ground_images',
        write_only=True,
        required=False
    )
    class Meta:
        model = Ground_EN
        fields = [
            'id',
            'internal_ground_name',
            'internal_ground_name_id',
            'ground_address_en',
            'ground_address_en_id',
            'ground_name_en',
            'ground_images_id',
            ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        image_urls = self.get_image_urls(instance)
        return {
            "id": data['id'],
            'internal_ground_name' : {
                "id": data["internal_ground_name"]['id'],
                "internal_ground_name": data["internal_ground_name"]["internal_ground_name"],
                "area": data["internal_ground_name"]['area'],
                "full_price": data["internal_ground_name"]['full_price'],
                'square_price': data['internal_ground_name']['square_price'],
                'status':data['internal_ground_name']['status'],
                'rank':data['internal_ground_name']['rank'],
                'phone_number':data['internal_ground_name']['phone_number'],
                "is_available": data["internal_ground_name"]['is_available'],
                "visibiliti": data["internal_ground_name"]['visibiliti'],
                "about_land": data["internal_ground_name"]["about_land"],

                
            },
            'ground_address_en': data["ground_address_en"],
            'ground_name_en':data['ground_name_en'],
            'ground_images': image_urls,
        }


    def get_image_urls(self, instance):
        images = Ground_Images.objects.filter(internal_ground_name=instance.internal_ground_name)
        return [S3Helper.generate_signed_url(str(image.images)) for image in images]
    
class Ground_RU_Serializer(serializers.ModelSerializer):
    internal_ground_name = Ground_Names_Serializer(read_only = True)
    internal_ground_name_id = serializers.PrimaryKeyRelatedField(
        queryset = Ground_Names.objects.all(),
        source = 'internal_ground_name',
        write_only=True,
        required=False
        
    )
    ground_address_ru = Address_RU_Serializer(read_only = True)
    ground_address_ru_id = serializers.PrimaryKeyRelatedField(
        queryset = Address_RU.objects.all(),
        source = 'ground_address_ru',
        write_only=True,
        required=False
    )
    ground_images_id = serializers.PrimaryKeyRelatedField(
        queryset = Ground_Images.objects.all(),
        source = 'ground_images',
        write_only=True,
        required=False 
    )
    class Meta:
        model = Ground_RU
        fields = [
            'id',
            'internal_ground_name',
            'internal_ground_name_id',
            'ground_address_ru',
            'ground_address_ru_id',
            'ground_name_ru',
            'ground_images_id',
            ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        image_urls = self.get_image_urls(instance)
        return {
            "id": data['id'],
            'internal_ground_name' : {
                "id": data["internal_ground_name"]['id'],
                "internal_ground_name": data["internal_ground_name"]["internal_ground_name"],
                "area": data["internal_ground_name"]['area'],
                "full_price": data["internal_ground_name"]['full_price'],
                'square_price': data['internal_ground_name']['square_price'],
                'status':data['internal_ground_name']['status'],
                'rank':data['internal_ground_name']['rank'],
                'phone_number':data['internal_ground_name']['phone_number'],
                "is_available": data["internal_ground_name"]['is_available'],
                "visibiliti": data["internal_ground_name"]['visibiliti'],
                "about_land": data["internal_ground_name"]["about_land"],


            },
            'ground_address_ru': data["ground_address_ru"],
            'ground_name_ru':data['ground_name_ru'],
            'ground_images': image_urls,
        }


    def get_image_urls(self, instance):
        images = Ground_Images.objects.filter(internal_ground_name=instance.internal_ground_name)
        return [S3Helper.generate_signed_url(str(image.images)) for image in images]

    


'''
-----------------------------------------------------------------------
            BLOG SERIALIZERS
-----------------------------------------------------------------------
'''

class Blog_Names_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog_Names
        fields = [
            'id',
            'internal_blog_name',
            'created_at'
        ]

class Blog_Images_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog_Images
        fields = '__all__'

class Blog_KA_Serializer(serializers.ModelSerializer):
    internal_blog_name = Blog_Names_Serializer(read_only=True)
    blog_images = Blog_Images_Serializer(read_only=True)
    blog_images_id = serializers.PrimaryKeyRelatedField(
        queryset = Blog_Images.objects.all(),
        source = "blog_name_ka",
        write_only=True,
    )
    internal_blog_name_id = serializers.PrimaryKeyRelatedField(
        queryset = Blog_Names.objects.all(),
        source = 'internal_blog_name',
        write_only = True
    )
    class Meta:
        model = Blog_KA
        fields = [
            'id',
            'internal_blog_name',
            'internal_blog_name_id',
            'blog_name_ka',
            'description_ka',
            'second_description_ka',
            'blog_images',
            'blog_images_id'
        ]
    def to_representation(self, instance):
        data = super().to_representation(instance)
        image_urls = self.get_image_urls(instance)
        return {
            "id": data['id'],
            'internal_blog_name' : data["internal_blog_name"],
            'blog_name_ka':data['blog_name_ka'],
            'description_ka':data['description_ka'],
            'blog_images': image_urls,
            'second_description_ka': data['second_description_ka'],
        }
    
    def get_image_urls(self, instance):
        images = Blog_Images.objects.filter(internal_blog_name=instance.internal_blog_name)
        return [S3Helper.generate_signed_url(str(image.images)) for image in images]
    
class Blog_EN_Serializer(serializers.ModelSerializer):
    internal_blog_name = Blog_Names_Serializer(read_only=True)
    blog_images = Blog_Images_Serializer(read_only=True)
    blog_images_id = serializers.PrimaryKeyRelatedField(
        queryset = Blog_Images.objects.all(),
        source = "blog_name_en",
        write_only=True,
    )
    internal_blog_name_id = serializers.PrimaryKeyRelatedField(
        queryset = Blog_Names.objects.all(),
        source = 'internal_blog_name',
        write_only = True
    )
    class Meta:
        model = Blog_EN
        fields = [
            'id',
            'internal_blog_name',
            'internal_blog_name_id',
            'blog_name_en',
            'description_en',
            'second_description_en',
            'blog_images',
            'blog_images_id'
        ]
    def to_representation(self, instance):
        data = super().to_representation(instance)
        image_urls = self.get_image_urls(instance)
        return {
            "id": data['id'],
            'internal_blog_name' : data["internal_blog_name"],
            'blog_name_en':data['blog_name_en'],
            'description_en':data['description_en'],
            'blog_images': image_urls,
            'second_description_en': data['second_description_en'],

        }
    
    def get_image_urls(self, instance):
        images = Blog_Images.objects.filter(internal_blog_name=instance.internal_blog_name)
        return [S3Helper.generate_signed_url(str(image.images)) for image in images]

class Blog_RU_Serializer(serializers.ModelSerializer):
    internal_blog_name = Blog_Names_Serializer(read_only=True)
    blog_images = Blog_Images_Serializer(read_only=True)
    blog_images_id = serializers.PrimaryKeyRelatedField(
        queryset = Blog_Images.objects.all(),
        source = "blog_name_ru",
        write_only=True,
    )
    internal_blog_name_id = serializers.PrimaryKeyRelatedField(
        queryset = Blog_Names.objects.all(),
        source = 'internal_blog_name',
        write_only = True
    )
    class Meta:
        model = Blog_RU
        fields = [
            'id',
            'internal_blog_name',
            'internal_blog_name_id',
            'blog_name_ru',
            'description_ru',
            'second_description_ru',
            'blog_images',
            'blog_images_id'
        ]
    def to_representation(self, instance):
        data = super().to_representation(instance)
        image_urls = self.get_image_urls(instance)
        return {
            "id": data['id'],
            'internal_blog_name' : data["internal_blog_name"],
            'blog_name_ru':data['blog_name_ru'],
            'description_ru':data['description_ru'],
            'blog_images': image_urls,
            'second_description_ru': data['second_description_ru'],
        }
    
    def get_image_urls(self, instance):
        images = Blog_Images.objects.filter(internal_blog_name=instance.internal_blog_name)
        return [S3Helper.generate_signed_url(str(image.images)) for image in images]


'''
-----------------------------------------------------------------------
            PROMOTIONS AND OFFETS SERIALIZERS
-----------------------------------------------------------------------
'''

# from rest_framework import serializers

# # Assuming Company_Image_serializers and Company_Names are already imported

# class PromotionsAndOffersNamesSerializer(serializers.ModelSerializer):
#     company_image = serializers.SerializerMethodField()  # Add this line

#     class Meta:
#         model = Promotions_and_offers_Names
#         fields = ['internal_promotion_name', 'start_date', 'end_date', 'company', 'discount', 'gift', 'installment', 'visibility', 'company_image']  # Include the new field here

#     def get_company_image(self, obj):
#         # Assuming `company` field in Promotions_and_offers_Names points to a Company_Names instance
#         company_image_instance = Company_Images.objects.filter(internal_name=obj.company).first()
#         if company_image_instance:
#             return Company_Image_serializers(company_image_instance).data
#         return None

class company_ImageSerializer_new(serializers.ModelSerializer):
    class Meta:
        model = Company_Images
        fields = ["logocompany"]



class PromotionsAndOffersNamesSerializer(serializers.ModelSerializer):
    company_image = serializers.SerializerMethodField()  # Add this line
    class Meta:
        model = Promotions_and_offers_Names
        fields = ['internal_promotion_name', 'start_date', 'end_date', 'company', 'discount', 'gift', 'installment', 'visibility', 'company_image']

    def get_company_image(self, obj):
        # Assuming `company` field in Promotions_and_offers_Names points to a Company_Names instance
        company_image_instance = Company_Images.objects.filter(internal_name=obj.company).first()
        if company_image_instance:
            return company_ImageSerializer_new(company_image_instance).data
        return None




class PromotionsAndOffersImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotions_and_offers_Images
        fields = ['internal_promotion_name', 'images']

class PromotionsAndOffersKASerializer(serializers.ModelSerializer):
    promotion_images = PromotionsAndOffersImagesSerializer(read_only=True)
    internal_promotion_name_details = serializers.SerializerMethodField()
    company_mobile = serializers.SerializerMethodField() 
    company_address_ka = serializers.SerializerMethodField()

    class Meta:
        model = Promotions_and_offers_KA
        fields = ['internal_promotion_name', 'promotion_name_ka', 'promotion_images', 'about_ka', 'alert_ka', 'internal_promotion_name_details','company_mobile','company_address_ka']

    def get_internal_promotion_name_details(self, obj):
        return PromotionsAndOffersNamesSerializer(obj.internal_promotion_name).data
    
    def get_company_mobile(self, obj):
        return obj.internal_promotion_name.company.Mobile

    def get_company_address_ka(self, obj):
        # Assuming there's a way to navigate from your promotion to the Company_EN model
        company_ka_instance = Company_KA.objects.filter(internal_name__internal_name=obj.internal_promotion_name.company).first()
        if company_ka_instance:
            return company_ka_instance.address_ka
        return None
    


class PromotionsAndOffersENSerializer(serializers.ModelSerializer):
    promotion_images = PromotionsAndOffersImagesSerializer(read_only=True)
    internal_promotion_name_details = serializers.SerializerMethodField()
    company_mobile = serializers.SerializerMethodField() 
    company_address_en = serializers.SerializerMethodField()

    class Meta:
        model = Promotions_and_offers_EN
        fields = ['internal_promotion_name', 'promotion_name_en', 'promotion_images', 'about_en','alert_en', 'internal_promotion_name_details' , 'company_mobile','company_address_en']

    def get_internal_promotion_name_details(self, obj):
        return PromotionsAndOffersNamesSerializer(obj.internal_promotion_name).data
    

    def get_company_mobile(self, obj):
        # Direct access if you have a direct relationship setup
        return obj.internal_promotion_name.company.Mobile

    def get_company_address_en(self, obj):
        # Assuming there's a way to navigate from your promotion to the Company_EN model
        company_en_instance = Company_EN.objects.filter(internal_name__internal_name=obj.internal_promotion_name.company).first()
        if company_en_instance:
            return company_en_instance.address_en
        return None

class PromotionsAndOffersRUSerializer(serializers.ModelSerializer):
    promotion_images = PromotionsAndOffersImagesSerializer(read_only=True)
    internal_promotion_name_details = serializers.SerializerMethodField()
    company_mobile = serializers.SerializerMethodField() 
    company_address_ru = serializers.SerializerMethodField()


    class Meta:
        model = Promotions_and_offers_RU
        fields = ['internal_promotion_name', 'promotion_name_ru', 'promotion_images', 'about_ru', 'alert_ru','internal_promotion_name_details', 'company_mobile','company_address_ru']

    def get_internal_promotion_name_details(self, obj):
        return PromotionsAndOffersNamesSerializer(obj.internal_promotion_name).data

    def get_company_mobile(self, obj):
        return obj.internal_promotion_name.company.Mobile

    def get_company_address_ru(self, obj):
        # Assuming there's a way to navigate from your promotion to the Company_EN model
        company_ru_instance = Company_RU.objects.filter(internal_name__internal_name=obj.internal_promotion_name.company).first()
        if company_ru_instance:
            return company_ru_instance.address_ru
        return None
    


'''
-----------------------------------------------------------------------
            Complex_With_Appartments
-----------------------------------------------------------------------
''' 
class NewAppartment_KA_Serializer(serializers.ModelSerializer):
    appartment_images = Appartment_Images_Serializer(read_only = True)
    appartment_address_ka = Address_KA_Serializer(read_only=True)
    internal_apartment_name  = Appartment_Names_Serializer(read_only=True)


    class Meta:
        model = Appartment_KA
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        image_urls = self.get_apparment_image_urls(instance)
        data["appartment_images"]= image_urls
        return data
    
    def get_apparment_image_urls(self, instance):
        images = Appartment_Images.objects.filter(internal_apartment_name=instance.internal_apartment_name)
        return [S3Helper.generate_signed_url(str(image.images)) for image in images]

class NewAppartment_EN_Serializer(serializers.ModelSerializer):
    appartment_images = Appartment_Images_Serializer(read_only = True)
    appartment_address_en = Address_EN_Serializer(read_only=True)
    internal_apartment_name  = Appartment_Names_Serializer(read_only=True)

    class Meta:
        model = Appartment_EN
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        image_urls = self.get_apparment_image_urls(instance)
        data["appartment_images"]= image_urls
        return data
    
    def get_apparment_image_urls(self, instance):
        images = Appartment_Images.objects.filter(internal_apartment_name=instance.internal_apartment_name)
        return [S3Helper.generate_signed_url(str(image.images)) for image in images]

class NewAppartment_RU_Serializer(serializers.ModelSerializer):
    appartment_images = Appartment_Images_Serializer(read_only = True)
    appartment_address_ru = Address_RU_Serializer(read_only=True)
    internal_apartment_name  = Appartment_Names_Serializer(read_only=True)

    
    class Meta:
        model = Appartment_RU
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        image_urls = self.get_apparment_image_urls(instance)
        data["appartment_images"]= image_urls
        return data
    
    def get_apparment_image_urls(self, instance):
        images = Appartment_Images.objects.filter(internal_apartment_name=instance.internal_apartment_name)
        return [S3Helper.generate_signed_url(str(image.images)) for image in images]


class Complex_with_appartments_KA_Serializer(serializers.ModelSerializer):
    appartment_name_ka = NewAppartment_KA_Serializer(many=True, read_only=True)
    internal_complex_name = Complex_Name_Serializers(read_only=True)
    complex_images = Complex_Image_Serializers(read_only=True)
    company_ka = Company_KA_serializers(read_only=True)
    complex_address_ka = Address_KA_Serializer(source='address_ka', read_only=True)
    



    class Meta:
        model = Complex_KA
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        image_urls = self.get_complex_image_urls(instance)
        data["complex_images"]= image_urls
        return data
    
    def get_complex_image_urls(self, instance):
        images = Complex_Images.objects.filter(internal_complex_name=instance.internal_complex_name)
        return [S3Helper.generate_signed_url(str(image.images)) for image in images]

class Complex_with_appartments_EN_Serializer(serializers.ModelSerializer):
    appartment_name_en = NewAppartment_EN_Serializer(many=True, read_only=True)
    internal_complex_name = Complex_Name_Serializers(read_only=True)
    complex_images = Complex_Image_Serializers(read_only=True)
    company_en = Company_EN_serializers(read_only=True)
    complex_address_en = Address_EN_Serializer(source='address_en', read_only=True)

    class Meta:
        model = Complex_EN
        fields = '__all__'
    def to_representation(self, instance):
        data = super().to_representation(instance)
        image_urls = self.get_complex_image_urls(instance)
        data["complex_images"]= image_urls
        return data
    
    def get_complex_image_urls(self, instance):
        images = Complex_Images.objects.filter(internal_complex_name=instance.internal_complex_name)
        return [S3Helper.generate_signed_url(str(image.images)) for image in images]

class Complex_with_appartments_RU_Serializer(serializers.ModelSerializer):
    appartment_name_ru = NewAppartment_RU_Serializer(many=True, read_only=True)
    internal_complex_name = Complex_Name_Serializers(read_only=True)
    complex_images = Complex_Image_Serializers(read_only=True)
    company_ru = Company_RU_serializers(read_only=True)
    complex_address_ru = Address_RU_Serializer(source='address_ru', read_only=True)

    class Meta:
        model = Complex_RU
        fields = '__all__'
    def to_representation(self, instance):
        data = super().to_representation(instance)
        image_urls = self.get_complex_image_urls(instance)
        data["complex_images"]= image_urls
        return data
    
    def get_complex_image_urls(self, instance):
        images = Complex_Images.objects.filter(internal_complex_name=instance.internal_complex_name)
        return [S3Helper.generate_signed_url(str(image.images)) for image in images]
    

'''
-----------------------------------------------------------------------
            Company_With_Complex
-----------------------------------------------------------------------
''' 
  
class ComplexKASerializer(serializers.ModelSerializer):
    complex_images = serializers.SerializerMethodField()
    address_ka = Address_KA_Serializer()
    internal_complex_name = Complex_Name_Serializers()
    class Meta:
        model = Complex_KA
        fields = [
            "internal_complex_name",
            "complex_images",
            "company_ka",
            "address_ka",
            "complex_name_ka", 
            "type_of_roof_ka",
            "construction_type_ka",
            "submission_type_ka",
            "protection_type_ka",
            "description_ka",
        ]

    def get_complex_images(self, instance):
        images = Complex_Images.objects.filter(internal_complex_name=instance.internal_complex_name)
        return [S3Helper.generate_signed_url(str(image.images)) for image in images]


class CompanyKASerializer(serializers.ModelSerializer):
    complexes = ComplexKASerializer(many=True)
    internal_name = Company_Image_serializers()

    class Meta:
        model = Company_KA
        fields = '__all__'




class ComplexENSerializer(serializers.ModelSerializer):
    complex_images = serializers.SerializerMethodField()
    address_en = Address_EN_Serializer()
    internal_complex_name = Complex_Name_Serializers()
    class Meta:
        model = Complex_EN
        fields = [
            "internal_complex_name",
            "complex_images",
            "company_en",
            "address_en",
            "complex_name_en", 
            "type_of_roof_en",
            "construction_type_en",
            "submission_type_en",
            "protection_type_en",
            "description_en",
        ]

    def get_complex_images(self, instance):
        images = Complex_Images.objects.filter(internal_complex_name=instance.internal_complex_name)
        return [S3Helper.generate_signed_url(str(image.images)) for image in images]


class CompanyENSerializer(serializers.ModelSerializer):
    complexes = ComplexENSerializer(many=True)
    internal_name = Company_Image_serializers()
    class Meta:
        model = Company_EN
        fields = '__all__'




class ComplexRUSerializer(serializers.ModelSerializer):
    complex_images = serializers.SerializerMethodField()
    address_ru = Address_RU_Serializer()
    internal_complex_name = Complex_Name_Serializers()
    class Meta:
        model = Complex_RU
        fields = [
            "internal_complex_name",
            "complex_images",
            "company_ru",
            "address_ru",
            "complex_name_ru", 
            "type_of_roof_ru",
            "construction_type_ru",
            "submission_type_ru",
            "protection_type_ru",
            "description_ru",
        ]

    def get_complex_images(self, instance):
        images = Complex_Images.objects.filter(internal_complex_name=instance.internal_complex_name)
        return [S3Helper.generate_signed_url(str(image.images)) for image in images]


class CompanyRUSerializer(serializers.ModelSerializer):
    complexes = ComplexRUSerializer(many=True)
    internal_name = Company_Image_serializers()
    class Meta:
        model = Company_RU
        fields = '__all__'
