from django.contrib.auth.models import BaseUserManager



class UserManager(BaseUserManager):
    
    
    def create_user(self, email,  password, *arg, **kwargs):
        
        if not email:
            
            raise ValueError("email field is required")
        
        if not password:
            raise ValueError("password field is required")
        
        email =  self.normalize_email(email=email)
        
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        
        return user.save()
    
    
    def create_superuser(self, email, password, *arg, **kwargs):
        
        
        kwargs['is_staff'] = True
        kwargs['is_superuser'] = True
        kwargs['is_active'] = True
        
        
        return self.create_user(email, password, *arg, **kwargs)