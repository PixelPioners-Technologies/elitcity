from mptt.admin import DraggableMPTTAdmin
from .models import CityLocations
from complex.models import Complex
from django.contrib import admin

class CityLocationsAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = ('tree_actions', 'indented_title',
                    'related_complexes_count', 'related_complexes_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative complex count
        qs = CityLocations.objects.add_related_count(
                qs,
                Complex,
                'city_location',
                'complexes_cumulative_count',
                cumulative=True)
 
        # Add non-cumulative complex count
        qs = CityLocations.objects.add_related_count(
                qs,
                Complex,
                'city_location',
                'complexes_count',
                cumulative=False)
        return qs

    def related_complexes_count(self, instance):
        return getattr(instance, 'complexes_count', 0)
    related_complexes_count.short_description = 'Number of complexes (for this location)'

    def related_complexes_cumulative_count(self, instance):
        return getattr(instance, 'complexes_cumulative_count', 0)
    related_complexes_cumulative_count.short_description = 'Number of complexes (in tree)'

admin.site.register(CityLocations, CityLocationsAdmin)





# from django.contrib import admin
# from mptt.admin import DraggableMPTTAdmin
# from .models import CityLocations

# admin.site.register(
#     CityLocations,
#     DraggableMPTTAdmin,
#     list_display=(
#         'tree_actions',
#         'indented_title',
        
#     ),
#     list_display_links=(
#         'indented_title',
#     ),
# )