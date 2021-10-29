from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):

	email = forms.EmailField(required=True)
    # phone = forms.CharField(required=True,max_length=11)
    # address = forms.CharField(required=True,max_length=200)
    # birthday = forms.DateField(required=True)
    # gender = forms.ChoiceField(choices=(("Male","M"),("Female","F"),"Other","Other"),required=True)
    # blood_group = forms.ChoiceField(choices=(("A+","A+"),("A-","A-"),("B+","B+"),("B-","B-"),("AB+","AB+"),("AB-","AB-"),("O+","O+"),("O-","O-")))
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user