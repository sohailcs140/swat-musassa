from typing import Any
from django import forms
from .models import SaudiKapilDetail, Employe, VisaRenewal
from datetime import date

class SaudiKapilForm(forms.ModelForm):
    
    class Meta:
        model = SaudiKapilDetail
        exclude = ["id", "active"]
    
    def __init__(self, *args, **kwargs):
        
        super(SaudiKapilForm, self).__init__(*args, **kwargs)
        
        
        for field_name, field in self.fields.items():
            
            field.label = None
            field.widget.attrs.update({
                "class":"form-control",
                "aria-label": f"Enter {field_name}",
                "placeholder":f"Enter {field_name}"
            })
        
        address_field = self.fields['address']
        
        address_field.widget.attrs = {
            **address_field.widget.attrs,
            "class":"form-control h-px-100"
        }
        cnic_field = self.fields['cnic']
        cnic_field.widget.attrs={
            **cnic_field.widget.attrs,
            "class":"form-control iqamaMask",
            "placeholder":"1XXXXXXXXX",
            "aria-label": "Enter Iqama Number"
        }
        
        self.fields['phone'].widget.attrs={
            **self.fields['phone'].widget.attrs,
            "class":"form-control phone-number-mask",
            "placeholder":"5987896843",
            "aria-label": "Enter phone"
        }
    
    
    

class EmployeForm(forms.ModelForm):
    
    class Meta:
        model = Employe
        
        exclude = ['id', 'active']
    
    def __init__(self, *args, **kwargs):
        
        super(EmployeForm, self).__init__(*args, **kwargs)
        
        
        for field_name, field in self.fields.items():
            
            field.widget.label = None
            field.widget.attrs ={
                **field.widget.attrs,
                "class":"form-control",
                "placeholder":"Enter {name}".format(name=field_name.capitalize())
            }
            
            cnic_field = self.fields['cnic']
            cnic_field.widget.attrs={
            **cnic_field.widget.attrs,
            "class":"form-control iqamaMask",
            "placeholder":"2XXXXXXXXX",
            "aria-label": "Enter Iqama Number"
            }
        
        self.fields['phone'].widget.attrs={
            **self.fields['phone'].widget.attrs,
            "class":"form-control phone-number-mask",
            "placeholder":"5987896843",
            "aria-label": "Enter phone"
        }
        
        self.fields['issue_date'].widget.attrs = {
            **self.fields['issue_date'].widget.attrs,
            "class":"form-control date-mask",
            "placeholder":"YYYY-MM-DD"
        }
        
        self.fields['expiry_date'].widget.attrs = {
            **self.fields['expiry_date'].widget.attrs,
            "class":"form-control date-mask",
            "placeholder":"YYYY-MM-DD"
        }
        self.fields['country'].widget.attrs.update({
            'class':"select2 form-select form-select-lg",
            "id":"country_id",
        })
        self.fields['saudi_kapil'].widget.attrs.update({
            'class':"select2 form-select form-select-lg",
            "id":"employer_id",
        })

    


class VisaRenewalForm(forms.ModelForm):
    
    
    class Meta:
        
        model = VisaRenewal
        fields = ('employe', 'curr_saudi_kapil', 'curr_profession','remarks', 'curr_visa_type', 'curr_issue_date', 'curr_expiry_date' )
    
    
    
    def __init__(self, *args, **kwargs):
        
        super(VisaRenewalForm, self).__init__(*args, **kwargs)
        
        
        for field_name, field in self.fields.items():
            
            field.widget.label = None
            field.widget.attrs ={
                **field.widget.attrs,
                "class":"form-control",
                "placeholder":"Enter {name}".format(name=field_name.replace("curr_", "").replace("_", " ").capitalize())
            }
            
            if field_name == "remarks":
                
                field.widget.attrs.update({
                    'class':"form-control h-px-100"
                })
                
            if field_name in ['employe', 'curr_saudi_kapil', 'curr_visa_type']:
                
                   field.widget.attrs.update({
                     'class':"select2 form-select form-select-lg"
                    })
            
            if field_name in ['curr_issue_date', 'curr_expiry_date']:
                
                    field.widget.attrs.update({
                            "class":"form-control date-mask",
                            "placeholder":"YYYY-MM-DD"
                        }
                    )
        