from django.db.models.signals import pre_save, post_save
from .models import VisaRenewal, Employe
from django.dispatch import receiver


@receiver(signal=pre_save, sender=VisaRenewal)
def visa_renewal_pre_save(sender:VisaRenewal, instance:VisaRenewal, *args, **kwargs):
    
    if not sender.objects.filter(pk=instance.pk).exists():
        
        # only run when a new record is created
        instance.prev_expiry_date = instance.employe.expiry_date
        instance.prev_issue_date = instance.employe.issue_date
        instance.prev_profession = instance.employe.profession
        instance.prev_saudi_kapil = instance.employe.saudi_kapil
        instance.prev_visa_type = instance.employe.visa_type
    
    


@receiver(signal=post_save, sender=VisaRenewal)
def visa_renewal_post_save(sender, instance:VisaRenewal, created:bool, *args, **kwargs):
    
    if created or instance.is_latest:
        
        # this code will be executed when the new object is created or updated the existing one
        employe:Employe = Employe.objects.get(pk=instance.employe.pk)
        
        employe.profession = instance.curr_profession
        employe.visa_type = instance.curr_visa_type
        employe.saudi_kapil = instance.curr_saudi_kapil
        employe.issue_date = instance.curr_issue_date
        employe.expiry_date = instance.curr_expiry_date
        
        employe.save()
    
            
        
        
def is_same(employee:Employe, renewal:VisaRenewal) -> bool:
    
        return (renewal.curr_expiry_date == employee.expiry_date and 
        renewal.curr_issue_date == employee.issue_date and 
        renewal.curr_profession == employee.profession and
        renewal.curr_saudi_kapil == employee.saudi_kapil and
        renewal.curr_visa_type == employee.visa_type)


# Singals related to employee
@receiver(signal=post_save, sender=Employe)
def employee_post_save(sender, instance:Employe, created:bool, *args, **kwargs):
    
    if not created:
        
        visa_renewals = instance.visa_renewals.all().order_by('-curr_issue_date')[:1]
        
        if visa_renewals.exists():
            visa_renewal:VisaRenewal = visa_renewals[0]
            
            if not is_same(employee=instance, renewal=visa_renewal):
            
                visa_renewal.curr_expiry_date = instance.expiry_date
                visa_renewal.curr_issue_date = instance.issue_date
                visa_renewal.curr_profession = instance.profession
                visa_renewal.curr_saudi_kapil = instance.saudi_kapil
                visa_renewal.curr_visa_type = instance.visa_type
            
                visa_renewal.save()
    
    



