from django import forms  
from .models import Razze, Cani 

class CaniModelForm(forms.ModelForm):  
    class Meta:  
        model = Cani 
        fields = "__all__"  
        
