from django import forms
from .models import PQRS

class PQRSFilterForm(forms.Form):
    ESTADOS_CHOICES = [
        ('', 'Todos'),  
        ('Pendiente', 'Pendiente'),
        ('En Proceso', 'En Proceso'),
        ('Resuelta', 'Resuelta'),
    ]

    estado = forms.ChoiceField(
        label='Filtrar por Estado',
        choices=ESTADOS_CHOICES,
        required=False  
    )


    
class PQRSForm(forms.ModelForm):
    class Meta:
        model = PQRS  
        fields = ['tipoPQRS', 'fechaPQRS', 'DescripcionPQRS']
        