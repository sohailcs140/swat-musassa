from django_filters import FilterSet, CharFilter, DateFilter
from .models import SaudiKapilDetail, Employe, VisaRenewal


class SaudiKapilFilter(FilterSet):
    
    name = CharFilter(field_name="name", lookup_expr="icontains")
    iqama_number = CharFilter(field_name="cnic", lookup_expr="istartswith")
    phone = CharFilter(field_name="phone", lookup_expr="istartswith")
    gender = CharFilter(field_name="gender", lookup_expr="iexact")
        
    class Meta:
        model = SaudiKapilDetail
        
        fields = ['name', 'cnic', 'phone', 'gender']



class EmployeFilter(FilterSet):
    
    name = CharFilter(field_name="name", lookup_expr="icontains")
    iqama_number = CharFilter(field_name="cnic", lookup_expr="istartswith")
    phone = CharFilter(field_name="phone", lookup_expr="istartswith")
    gender = CharFilter(field_name="gender", lookup_expr="iexact")
    issue_date = DateFilter(field_name="issue_date", lookup_expr="exact")
    expiry_date = DateFilter(field_name="expiry_date", lookup_expr="exact")
        
    class Meta:
        model = Employe
        
        fields = ['name', 'cnic','phone', 'gender',"issue_date",
                  "expiry_date"
                  ]
        



class VisaRenewalFilter(FilterSet):
    
    visa_issue_date = DateFilter(field_name="curr_issue_date", lookup_expr="exact")
    employe_iqama = CharFilter(field_name="employe__cnic", lookup_expr="exact")
    visa_type = CharFilter(field_name="curr_visa_type__name", lookup_expr="iexact")
    employer = CharFilter(field_name="curr_saudi_kapil__id", lookup_expr="exact")
    
    class Meta:
        
        model = VisaRenewal
        fields = [
            'curr_issue_date',
            'employe',
            'curr_visa_type',
            'curr_saudi_kapil'
        ]

    
    