from django.core.management.base import BaseCommand
from app.models import *
from core.models import *
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    
    
    
    def handle(self, *args, **kwargs):
        
        try:
            for model in [VisaRenewal, Employe, SaudiKapilDetail, VisaType, get_user_model()]:
                
                model.objects.all().delete()
        
            print("database has been reset")
        except Exception as e:
            
            print(e)
        