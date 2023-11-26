from modeltranslation.translator import translator, TranslationOptions
from .models import Complex , Company

class ComplexTranslationOptions(TranslationOptions):
    fields = ('name', 
                'address',
                'type_of_roof',
                 'text1',
                 'text2',
                 'text3',
                 'text4',
                 'text5',
                 'text6',
                 'text7',
                 'text8',
                  )

translator.register(Complex, ComplexTranslationOptions)


class CompanyTranslationOptions(TranslationOptions):
    fields = ( 'name', 'address', 'aboutcompany' ,  )



translator.register(Company , CompanyTranslationOptions )