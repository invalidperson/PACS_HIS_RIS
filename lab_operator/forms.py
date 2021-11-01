from django import forms
from .models import Radiological_Data
class UploadEntryForm(forms.ModelForm):

    class Meta:
        model= Radiological_Data
        fields = ('patient','experiment_name','patient_history','procedure','findings','impression','file')