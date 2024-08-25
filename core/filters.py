from django_filters import FilterSet, CharFilter, NumberFilter
from .models import VisaType


class VisaTypeFileter(FilterSet):
    
    name = CharFilter(field_name="name", lookup_expr="icontains")
    
    class Meta:
        
        model = VisaType
        fields = ['name']
        