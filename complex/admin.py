from django.contrib import admin
from .models import * #, ComplexImage 

admin.site.register(Language)

admin.site.register(City_KA)
admin.site.register(City_EN)
admin.site.register(City_RU)

admin.site.register(PharentDistrict_EN)
admin.site.register(PharentDistrict_KA)
admin.site.register(PharentDistrict_RU)

admin.site.register(District_KA)
admin.site.register(District_EN)
admin.site.register(District_RU)

admin.site.register(Address_KA)
admin.site.register(Address_EN)
admin.site.register(Address_RU)

admin.site.register(Street_Name_EN)
admin.site.register(Street_Name_KA)
admin.site.register(Street_Name_RU)

admin.site.register(Complex_Names)

admin.site.register(Complex_KA)
admin.site.register(Complex_EN)
admin.site.register(Complex_RU)

admin.site.register(Appartment_EN)
admin.site.register(Appartment_KA)
admin.site.register(Appartment_RU)










#  "longitude": 41.725962,
#     "latitude": 44.74724