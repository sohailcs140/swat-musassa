from django import template
from datetime import date
from django.conf import settings
from app.models import Employe, SaudiKapilDetail, VisaRenewal, TrackEmail

register = template.Library()


@register.filter
def format_date(val):
    
    str_date = str(val)
    
    
    return str_date.replace("-", "")


@register.filter
def get_badge_class(val):
    
    diff = val - date.today() 
    
    if diff.days <= 7:
        return "danger"
    else:
        return "warning"


@register.filter
def gender_badge_class(val:str):
    
    if val.lower() == "male":
        return "info"
    
    elif val.lower() == "female":
        
        return "success"
    
    return "secondary"


@register.filter
def get_country_name(val:str)->str:
        
    for key, value in settings.COUNTRIES_WITH_FLAGS.items():
        if key.lower() == val.lower():
            
            return key
    
    return ""





@register.simple_tag
def get_employee_names_as_list():
    return [name for name in 
            Employe.objects.values_list("name", flat=True)]



@register.simple_tag
def get_employee_cnic_as_list():
    
    return [cnic for cnic in Employe.objects.values_list("cnic", flat=True)]


@register.simple_tag
def get_employer_cnic_as_list():
    return [cnic for cnic in SaudiKapilDetail.objects.values_list("cnic", flat=True)]


@register.simple_tag
def get_employer_names_as_list():
    return [name for name in SaudiKapilDetail.objects.values_list("name", flat=True)]



@register.simple_tag
def get_cnic_from_visa_renewal():
    
    
    return [cnic for cnic  in VisaRenewal.objects.values_list("employe__cnic", flat=True)]


@register.simple_tag
def get_issue_dates_from_visa_renewal():

    return [curr_issue_date for curr_issue_date  in VisaRenewal.objects.all().order_by("-curr_issue_date").values_list("curr_issue_date", flat=True)]



@register.simple_tag
def get_track_emails():
    
    return TrackEmail.objects.filter(created_at__date=date.today()).order_by("-created_at")

@register.simple_tag
def today_expire():
    return Employe.objects.filter(expiry_date=date.today())