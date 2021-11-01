from django.db import models
# from django.db.models.deletion import CASCADE
from accounts.models import User
from django.urls import reverse
# Create your models here.
class Prescription(models.Model):

    patient = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Assigned Patient")
    doctor = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Assigned Doctor",related_name="Prescription_By_Doctor")
    date = models.DateTimeField()

    symptoms = models.CharField(max_length=10000,verbose_name="Symptoms Found",blank=False,null=False)
    tests_given = models.CharField(max_length=10000,verbose_name="Tests given",blank=False,null=False)
    treatment = models.CharField(max_length=10000,verbose_name="Treatment Given",blank=False,null=False)
    follow_up_date = models.DateField(verbose_name="Date for Follow Up")



    def __str__(self):
        return str(self.patient)+" by "+str(self.doctor) + " at " + str(self.date.date())


    def get_absolute_url(self):

        args=[ self.id ]

        return reverse('doctor:previous_prescriptions_details', args=args )