from rest_framework import serializers
from .models import *

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
        print(data)
        return {'id': data['id'],
                'city_ru': data['city_ru'],
                'language': data['language']}
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
            'lang': representation['pharentDistrict_ka']["language"],
            'city_ru': representation['pharentDistrict_ru']['city_ru'],
            'pharentDistrict_ru': representation['pharentDistrict_ru']['pharentDistrict_ru'],
            'district_ru': representation['district_ru'],
            'lang': representation['pharentDistrict_ru']['lang'],
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
        queryset = City_KA.objects.all(),
        source = 'city_en',
        write_only = True,
    )
    district_ka = District_EN_Serializer(read_only=True)
    class Meta:
        model = Street_Name_EN
        fields = ['id',"city_id",'city_en', 'pharentDistrict_en', 'district_en', 'street_name_en', "lang_id"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            'id': representation['id'],
            'lang': representation['district_en']['lang'],
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
    district_ka = District_EN_Serializer(read_only=True)
    class Meta:
        model = Street_Name_EN
        fields = ['id',"city_id",'city_ru', 'pharentDistrict_ru', 'district_ru', 'street_name_ru', "lang_id"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            'id': representation['id'],
            'lang': representation['district_ru']['lang'],
            'city_ru': representation['district_ru']['city_ru'],
            'pharentDistrict_ru': representation['district_ru']['pharentDistrict_ru'],
            'district_ru': representation['district_ru']['district_ru'],
            'street_name_ru':representation['street_name_ru'],
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
        representation = super().to_representation(instance)
        print(representation)
        return {
            'id': representation['id'],
            'lang': representation['street_name_ka']['lang'],
            'city_ka': representation['street_name_ka']['city_ka'],
            'pharentDistrict_ka': representation['street_name_ka']['pharentDistrict_ka'],
            'district_ka': representation['street_name_ka']['district_ka'],
            'street_name_ka':representation['street_name_ka']['street_name_ka'],
            'address_ka':representation['address_ka'],
            'longitude': representation['longitude'],
            'latitude': representation['latitude'],
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
        representation = super().to_representation(instance)
        print(representation)
        return {
            'id': representation['id'],
            'lang': representation['street_name_en']['lang'],
            'city_en': representation['street_name_en']['city_en'],
            'pharentDistrict_en': representation['street_name_en']['pharentDistrict_en'],
            'district_en': representation['street_name_en']['district_en'],
            'street_name_en':representation['street_name_en']['street_name_en'],
            'address_en':representation['address_en'],
            'longitude': representation['longitude'],
            'latitude': representation['latitude'],
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
        representation = super().to_representation(instance)
        print(representation)
        return {
            'id': representation['id'],
            'lang': representation['street_name_ru']['lang'],
            'city_ru': representation['street_name_ru']['city_ru'],
            'pharentDistrict_ru': representation['street_name_ru']['pharentDistrict_ru'],
            'district_ru': representation['street_name_ru']['district_ru'],
            'street_name_ru':representation['street_name_ru']['street_name_ru'],
            'address_ru':representation['address_ru'],
            'longitude': representation['longitude'],
            'latitude': representation['latitude'],
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
    class Meta:
        model = Company_KA
        fields = ['internal_name_id', "internal_name", 'name_ka', 'address_ka', 'aboutcompany_ka']
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            #'id':data['id'],
            'record_id':data['internal_name']['id'],
            'internal_name':data['internal_name']['internal_name'],
            'Mobile':data['internal_name']['Mobile'],
            'Mobile_Home':data['internal_name']['Mobile_Home'],
            'email':data['internal_name']['email'],
            'companyweb':data['internal_name']['companyweb'],
            'facebook_page':data['internal_name']['facebook_page'],
            'logocompany':data['internal_name']['logocompany'],
            'background_image':data['internal_name']['background_image'],
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
        fields = ['internal_name_id', "internal_name", 'name_ru', 'address_ru', 'aboutcompany_ru']
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
        fields = ['complex','images']

class Complex_Image_Serializers_For_Complexes(serializers.ModelSerializer):
    class Meta:
        model = Complex_Images
        fields = ["images"]
    def to_representation(self, instance):
        return instance.images.url
        

class Complex_KA_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Complex_KA
        fields = '__all__'
    
class Complex_EN_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Complex_EN
        fields = '__all__'
    
class Complex_RU_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Complex_RU
        fields = '__all__'