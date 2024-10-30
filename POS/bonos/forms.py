from django import forms
from .models import Bono

class BonoForm(forms.ModelForm):
    class Meta:
        model = Bono
        fields = ['nombre', 'tipo', 'monto', 'estado'] 
