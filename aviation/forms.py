from django import forms
from .models import Aeroport, Avion

class AeroportForm(forms.ModelForm):
    class Meta:
        model = Aeroport
        fields = ['nom', 'capacite', 'image']


class AvionForm(forms.ModelForm):
    class Meta:
        model = Avion
        fields = ['id_avion', 'compagnie_aerienne', 'logo', 'situation','lieu']  