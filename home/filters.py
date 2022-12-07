import django_filters 

from . models import Property

class PropertyFilter(django_filters.FilterSet):

    class Meta:
        model = Property
        fields = [
            'category',
            'title', 
            'price',
            'rooms',
            'bathrooms',
            'garage_size',
            'type_property',
            'state',
            'city',
            'district',

        ]