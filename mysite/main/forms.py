from django import forms  
from .models import Impiegati22  

class Impiegati22Form(forms.ModelForm):  
    class Meta:  
        model = Impiegati22  
        fields = "__all__"  