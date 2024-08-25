from django.db import models



class DefaultModelManager(models.Manager):
    
    
    def get_queryset(self):
        
        return super().get_queryset().filter(active=True)


class AllObjectModelManager(models.Manager):
    
    def get_queryset(self) -> models.QuerySet:
         return super().get_queryset()
     
     

class CustomeModelManager(models.Manager):
        
        def get_queryset(self):
        
            return super().get_queryset().filter(active=False)