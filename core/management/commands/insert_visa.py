from django.core.management.base import BaseCommand
from core.models import VisaType

saudi_visa_types = [
    "Tourist Visa",
    "Business Visa",
    "Work Visa (Employment Visa)",
    "Visit Visa (Family Visa)",
    "Transit Visa",
    "Hajj Visa",
    "Umrah Visa",
    "Student Visa",
    "Residence Visa (Iqama)",
    "Diplomatic Visa",
    "Special Visa",
    ]


class Command(BaseCommand):
    
    
    def handle(self, *args, **options) :
        
        try:
            VisaType.objects.all().delete()
            for visa in saudi_visa_types:
                
                VisaType.objects.create(name=visa)
            print("visas set successfully")
        except Exception as e:
            
        
            print("the following exception is occure while creating the visas", e)
    