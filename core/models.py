from django.db import models
import uuid
from .managers import DefaultModelManager, CustomeModelManager



class VisaType(models.Model):
    
    id = models.CharField(unique=True, max_length=50, null=False, primary_key=True, default=uuid.uuid4)
    name = models.CharField(unique=True, max_length=25, null=False, blank=False)

    create_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    
    
    def __str__(self) -> str:
        return self.name

    objects = DefaultModelManager()
    del_items = CustomeModelManager()
    



