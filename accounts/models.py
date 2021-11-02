from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=50,blank=False,null=False,help_text ="Please Enter Your First Name")
    last_name = models.CharField(max_length=50,blank=False,null=False,help_text ="Please Enter Your Last/Given Name")
    phone = models.CharField(max_length=11,blank=False,null=False,primary_key=True,help_text ="Please Enter Your Phone number. eg: 01700000000")
    address = models.CharField(max_length=200,blank=False,null=False,help_text ="Please Enter Your Residential Address")
    gender = models.CharField(choices=[("M","Male"),("F","Female"),("Other","Other")],blank=False,null=False,max_length=10)
    blood_group = models.CharField(choices=[("A+","A+"),("A-","A-"),("B+","B+"),("B-","B-"),("AB+","AB+"),("AB-","AB-"),("O+","O+"),("O-","O-")],max_length=5)
    is_doctor = models.BooleanField(default=False,verbose_name="Is a Doctor")
    is_labop = models.BooleanField(default=False,verbose_name="Is a Lab Operator")


    def __str__(self):
        return  self.first_name + "_using_"  + self.phone
