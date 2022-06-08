from django.forms import ModelForm
from .models import Parts

class PartsForm(ModelForm):
    class Meta:
        model = Parts
        fields = ['date', 'descript', 'valor', 'categoria']
