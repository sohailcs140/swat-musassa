from django import forms
from .models import VisaType



class VisaTypeForm(forms.ModelForm):
    
    
    class Meta:
        
        model = VisaType
        fields = ["name"]
        
    
    
    def __init__(self, *args, **kwargs):
        
        super(VisaTypeForm, self).__init__(*args, **kwargs)
        
        self.fields['name'].label = None
        self.fields['name'].widget.attrs.update({
            'class':"form-control",
            "aria-label": "name",
            "placeholder":"name"
        })
        