from datetime import date
from django import forms

class PrescriptionForm(forms.Form):
    patient = forms.CharField(label="Patient Phone Number")
    symptoms = forms.CharField(label="Symptoms of Patient")
    tests_given = forms.CharField(label="Test Given")
    treatment = forms.CharField(label="Treatment Given")
    follow_up_date = forms.DateField(
    widget=forms.DateInput(),help_text="Please enter in YYYY-MM-DD format")