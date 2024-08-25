from django.core.management.base import BaseCommand
from app.models import Employe, SaudiKapilDetail
from core.models import VisaType
from faker import Faker
from .insert_employers import GENDER_CHOICES, NUMBER_CHOICES
import random
from datetime import timedelta, date
from django.conf import settings



fake = Faker()



class Command(BaseCommand):
    
    
    def handle(self, *args, **kwargs):
        try:
            Employe.objects.all().delete()
            for _ in range(400):
                name = fake.name()
                fname = fake.name() 
                cnic = f"{2}{str(fake.unique.random_number(digits=9)).zfill(9)}"  
                phone = f"{random.choice(NUMBER_CHOICES)}{fake.unique.random_number(digits=9)}"
                gender = random.choice(GENDER_CHOICES)
                saudi_kapil = SaudiKapilDetail.objects.order_by('?').first()
                profession = fake.job()
                visa_type = VisaType.objects.order_by('?').first()  
                issue_date = fake.date_this_decade(before_today=True)
                expiry_date = issue_date + timedelta(days=random.randint(30, 365)) 
                country = random.choice([code for _, code in settings.COUNTRIES_WITH_FLAGS.items()])
                work_location = fake.city()
                language = fake.language_name()
                email = fake.email()[:30]
                
                
                # insert record
                Employe.objects.create(
                name=name,
                fname=fname,
                cnic=cnic,
                phone=phone,
                gender=gender,
                saudi_kapil=saudi_kapil,
                profession=profession,
                visa_type=visa_type,
                issue_date=issue_date,
                expiry_date=expiry_date,
                country=country,
                work_location=work_location,
                language=language,
                email=email
            )

            print("employees set successfully")

        except Exception as e:
            
            print(e)