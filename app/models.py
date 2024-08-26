from django.db import models
import uuid
from core.models import VisaType
from datetime import date
from django.conf import settings
from core.managers import DefaultModelManager, CustomeModelManager, AllObjectModelManager


COUNTRY_CHOICES = [(value.lower(), value) for value, key in settings.COUNTRIES_WITH_FLAGS.items()]
GENDER_CHOICES = [("male", "Male"), ("female", "FeMale"), ('other', "Other")]


class SaudiKapilDetail(models.Model):
    
    id = models.CharField(unique=True, max_length=50, null=False, primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    cnic = models.CharField(max_length=10, unique=True)
    image = models.ImageField(upload_to="images/employer/", null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True, unique=True)
    address = models.TextField(max_length=80)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="male")
    email = models.EmailField(max_length=30, null=True, blank=True)
    
    
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    
    
    def __str__(self) -> str:
        return "{name}  ({cnic})".format(name=self.name, cnic=self.cnic)


    class Meta:
        ordering = ['-id']

    objects = DefaultModelManager()
    del_items = CustomeModelManager()
    all_objects = AllObjectModelManager()
    
    

class Employe(models.Model):


    id = models.CharField(unique=True, max_length=50, null=False, primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    cnic = models.CharField(max_length=10, unique=True)
    image = models.ImageField(upload_to="images/employe/", null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True, unique=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="male")
    saudi_kapil = models.ForeignKey(to=SaudiKapilDetail, on_delete=models.CASCADE, related_name="employees")
    profession = models.CharField(max_length=50)
    visa_type = models.ForeignKey(to=VisaType, on_delete=models.CASCADE, related_name="employees")
    issue_date = models.DateField()
    expiry_date = models.DateField()
    
    country = models.CharField(max_length=80, choices=COUNTRY_CHOICES)
    work_location = models.CharField(max_length=50, null=True, blank=True)
    language = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=30, null=True, blank=True)
    
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    
    
    def __str__(self): return "{name} -- {cnic}".format(name=self.name, cnic=self.cnic)
    

    class Meta:
        ordering = ['-issue_date']

    @property
    def visa_expired(self):        
        return not (self.expiry_date - date.today()).days > 0

    
    @property
    def is_email_send(self)->bool:
        return self.emails.all().filter(issue_date=self.issue_date, expiry_date=self.expiry_date).exists()
    

    objects = DefaultModelManager()
    del_items = CustomeModelManager()
    all_objects = AllObjectModelManager()
    
    
    
            
        
    
    
    
    
    
    
    
    

class VisaRenewal(models.Model):
    
    
    # for current record
    id = models.CharField(unique=True, max_length=50, null=False, primary_key=True, default=uuid.uuid4)
    employe = models.ForeignKey(to=Employe, on_delete=models.CASCADE, related_name="visa_renewals")
    
    curr_saudi_kapil = models.ForeignKey(to=SaudiKapilDetail, on_delete=models.CASCADE, related_name="visa_renewals")
    curr_profession = models.CharField(max_length=50)
    curr_visa_type = models.ForeignKey(to=VisaType, on_delete=models.CASCADE, related_name="visa_renewals")
    curr_issue_date = models.DateField()
    curr_expiry_date = models.DateField()
    remarks = models.TextField(max_length=80, null=True, blank=True)
    
    # to track the prev record
    prev_saudi_kapil = models.ForeignKey(to=SaudiKapilDetail, on_delete=models.CASCADE, related_name="prev_visa_renewals")
    prev_profession = models.CharField(max_length=50)
    prev_visa_type = models.ForeignKey(to=VisaType, on_delete=models.CASCADE, related_name="prev_visa_renewals")
    prev_issue_date = models.DateField()
    prev_expiry_date = models.DateField()
    
    
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    class Meta:
        
        ordering = ['-curr_issue_date']

    
    
    @property
    def is_expired(self):        
        return not (self.curr_expiry_date - date.today()).days >= 1
    
    
    @property
    def is_latest(self):
        
        last_rec = self.employe.visa_renewals.all().order_by("-curr_issue_date")[:1]
        
        if last_rec.exists():
            return self.id == last_rec.first().id
        
        return False
    



class TrackEmail(models.Model):
    
    employe = models.ForeignKey("Employe",related_name="emails", on_delete=models.CASCADE)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    