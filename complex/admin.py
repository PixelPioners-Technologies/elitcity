from django.contrib import admin
from .models import Complex , ComplexImage, Company, Apartment , VIPComplex , TopCompany
from modeltranslation.admin import TranslationAdmin


admin.site.register(ComplexImage)
admin.site.register(Apartment)
admin.site.register(VIPComplex)
admin.site.register(TopCompany)



@admin.register(Complex)
class ComplexAdmin(TranslationAdmin):
    pass


@admin.register(Company)
class CompanyAdmin(TranslationAdmin):
    pass