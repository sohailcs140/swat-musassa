from django.core.management.base import BaseCommand
from app.models import Employe, SaudiKapilDetail, VisaRenewal
from core.models import VisaType
from faker import Faker
import random
from datetime import timedelta, date

fake = Faker()



class Command(BaseCommand):
    
    
    
    def handle(self, *args, **kwargs):

        try:
            for _ in range(100):

                employe = Employe.objects.all().order_by("?").first()

                for _ in range(5):

                    saudi_kapil = SaudiKapilDetail.objects.all().order_by("?").first()
                    visa = VisaType.objects.all().order_by("?").first()

                    issue_date = fake.date_this_decade(before_today=True)

                    visa_renew = VisaRenewal(

                    employe=employe,
                    curr_saudi_kapil=saudi_kapil,
                    curr_profession=fake.job()[:50],
                    curr_visa_type=visa,
                    curr_issue_date=issue_date,
                    curr_expiry_date=issue_date + timedelta(days=random.randint(30, 365)),
                    remarks=fake.address()[:80],

                    prev_saudi_kapil=employe.saudi_kapil,
                    prev_profession=employe.profession,
                    prev_visa_type=employe.visa_type,
                    prev_issue_date=employe.issue_date,
                    prev_expiry_date=employe.expiry_date,
                    )


                    visa_renew.save()



            print("Renewals enter successfully")

        except Exception as e:
            
            print(e)