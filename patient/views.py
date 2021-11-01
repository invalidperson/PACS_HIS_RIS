from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from doctor.models import Prescription
from lab_operator.models import Radiological_Data

@login_required(login_url="/../accounts/login")
def patient_dashboard(request):
    username = request.user.username
    return render(request,"patient/dashboard.html",{"username":username})

def patient_records(request):
    patient = request.user
    patient_name = patient.username
    prescriptions = Prescription.objects.filter(patient=patient)

    return render(request,"patient/patient_records.html",{"prescriptions":prescriptions,"patient_name":patient_name})


def patient_rad_records(request):
    patient = request.user
    patient_name = patient.username
    rad_datas = Radiological_Data.objects.filter(patient=patient)

    return render(request,"patient/patient_rad_records.html",{"rad_datas":rad_datas,"patient_name":patient_name})



