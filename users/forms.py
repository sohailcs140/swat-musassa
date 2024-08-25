from typing import Any, Mapping
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.contrib.auth import get_user_model
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList


User = get_user_model()

class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        
        model  = User
        fields = ['first_name', 'last_name', 'image','email','is_active', 'is_superuser', 'is_staff']
        
        

class UserCreateForm(forms.ModelForm):
    
    
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'maxlength':"15"
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'maxlength':"15"
    }))
    
    
    class Meta:
        
        model = User
        fields = ['email', 'password', 'first_name', 'image',
                  'last_name', 
                  'is_superuser', 'is_staff', 
                  'is_active']
    
    
    
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        
        check_btns = ['is_superuser', 'is_staff', 'is_active']
        
        for name, field in self.fields.items():
            
            if name not in check_btns:
                field.label = None
                field.widget.attrs = {
                    **field.widget.attrs,
                    'class':"form-control",
                    'placeholder':"Enter {name}".format(name=name.replace("_", " ").title()),
                }
                
           
        
        for field in check_btns:
            
            self.fields[field].widget.attrs.update({
                "class":"form-check-input",
                "type":"checkbox"
                
            })

        
    def clean(self):

        email  = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        conf_password = self.cleaned_data.get("confirm_password")
        
        if not email:
            
            raise ValidationError("email field is required")
        
        if not password:
            
            raise ValidationError("password field is required")
        
        if not conf_password:
            
            raise ValidationError("confirm password field is required")
        
        
        
        return self.cleaned_data
    
    
        

class UserAuthenticationForm(forms.Form):

    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
    
        
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'aria-describedby': "Email",
            'placeholder':"Enter email",
            'autofocus':"",
            "name":"email",
            "maxlength":"30"
        }
    ))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'aria-describedby': "Password",
        'placeholder':"Enter password",
        "name":"password",
        "maxlength":"15"
    }))
    
    
    
    def clean(self):
        
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        
        if not email or not password:
            
            raise ValueError("Both password and email is required.")
        
        try:
            
            user = User.objects.get(email=email)
            
        except User.DoesNotExist:
            
            raise ValidationError("email or password is incorrect.")
        
        
        self.user = user = authenticate(self.request, email=email, password=password)
        
        if user is None:
            
            raise ValidationError("email or password is incorrect.")
        
        
        return self.cleaned_data
    

    def get_user(self):
        
        return self.user
    



class UserPasswordChangeForm(PasswordChangeForm):
    
    
    def __init__(self,user, *args, **kwargs):
        
        super(UserPasswordChangeForm, self).__init__(user, *args, **kwargs)
        
        for name, field in self.fields.items():
            
            field.widget.attrs.update({
                'class':'form-control',
                'aria-describedby': "Password {name}".format(name=name.replace("_", " ").replace("1", "").replace("2", "")),
                'placeholder':"Enter {name}".format(name=name.replace("_", " ").replace("1", "").replace("2", "")),
                
            })
            
            field.widget.label = False



class UserPasswordResetForm(SetPasswordForm):

    def __init__(self,user, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(user, *args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({
                'class': "form-control",
                'placeholder':f"{name.replace("_", " ").replace("1", "").replace("2", "").capitalize()}",
                "maxlength":"15"
            })