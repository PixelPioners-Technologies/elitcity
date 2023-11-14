from django.db import models
from mptt.models import TreeForeignKey , MPTTModel


class CityLocations(MPTTModel):
    name = models.CharField(max_length=200 , help_text='Enter the name of the city.')
    parent = TreeForeignKey('self' , null=True , blank=True , on_delete=models.CASCADE , related_name='children')

    class MPTTMeta:
            order_insertion_by = ['name']
            
    def __str__(self):
        return self.name
    
