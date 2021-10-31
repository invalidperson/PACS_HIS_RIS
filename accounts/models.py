from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=50,blank=False,null=False)
    last_name = models.CharField(max_length=50,blank=False,null=False)
    phone = models.CharField(max_length=11,blank=False,null=False,primary_key=True)
    address = models.CharField(max_length=200,blank=False,null=False)
    gender = models.CharField(choices=[("Male","M"),("Female","F"),("Other","Other")],blank=False,null=False,max_length=10)
    blood_group = models.CharField(choices=[("A+","A+"),("A-","A-"),("B+","B+"),("B-","B-"),("AB+","AB+"),("AB-","AB-"),("O+","O+"),("O-","O-")],max_length=5)
    is_doctor = models.BooleanField(default=False,verbose_name="Is a Doctor")
    is_labop = models.BooleanField(default=False,verbose_name="Is a Lab Operator")
