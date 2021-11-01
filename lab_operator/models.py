from django.db import models
from accounts.models import User
from django.urls import reverse
from datetime import datetime,date
import os
import uuid
import random

def user_directory_path(instance, filename):
    # Get Current Date
    todays_date = datetime.now()

    path = "dicom/{}/{}/{}/".format(todays_date.year, todays_date.month, todays_date.day)
    extension = "." + filename.split('.')[-1]
    stringId = str(uuid.uuid4())
    randInt = str(random.randint(10, 99))

    # Filename reformat
    filename_reformat = stringId + randInt + extension

    return os.path.join(path, filename_reformat)

class Radiological_Data(models.Model):
    patient = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Patient Assigned",related_name="data_of_patient")
    operator = models.ForeignKey(User,on_delete=models.CASCADE,related_name="uploaded_by_operator")
    
    experiment_name = models.CharField(max_length=200,verbose_name="Experiment Name",blank=False,null=False)
    patient_history = models.CharField(max_length=10000,verbose_name="Patient History",blank=False,null=False)
    procedure = models.CharField(max_length=10000,verbose_name="Experiment Procedure",blank=False,null=False)
    findings = models.CharField(max_length=10000,verbose_name="Findings",blank=False,null=False)
    impression = models.CharField(max_length=10000,verbose_name="Impression",blank=True,null=True)
    file = models.FileField(upload_to=user_directory_path)
    upload_date =  models.DateField(default=str(date.today()),editable=False)
   
   
   
    def __str__(self):
        filename = str(self.patient)  + " by " + str(self.operator) + " at "+ str(self.upload_date)
        return filename
   

    def get_absolute_url(self):

        args=[ self.id ]

        return reverse('lab_operator:previous_entry_details', args=args )




