from django.core.management.base import BaseCommand
from faker import Faker
import random
from app.models import SaudiKapilDetail


fake = Faker()
GENDER_CHOICES = ['male', 'female', 'other']
NUMBER_CHOICES = [5, 6, 7, 8, 9]

class Command(BaseCommand):
    
    
    def handle(slef, *args, **kwargs):
        try:
            SaudiKapilDetail.objects.all().delete()
            for _ in range(100):
                
                
                SaudiKapilDetail.objects.create(
                    name = fake.name(),
                    cnic = str(1) + str(fake.unique.random_number(digits=9)),
                    phone = str(random.choice(NUMBER_CHOICES)) + str(fake.unique.random_number(digits=9)),  
                    address = fake.address()[:80] ,
                    gender = random.choice(GENDER_CHOICES),
                    email = fake.email()[:30]
                )
            
            print("employees are enter successfully")
        except Exception as e:
            
            print(e)
        