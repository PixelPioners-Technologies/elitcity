from django.contrib import admin
from .models import Complex , ComplexImage, Company, Apartment , VIPComplex
from modeltranslation.admin import TranslationAdmin


# admin.site.register(Complex)
admin.site.register(ComplexImage)
# admin.site.register(Company)
admin.site.register(Apartment)
admin.site.register(VIPComplex)

@admin.register(Complex)
class ComplexAdmin(TranslationAdmin):
    pass


@admin.register(Company)
class CompanyAdmin(TranslationAdmin):
    pass