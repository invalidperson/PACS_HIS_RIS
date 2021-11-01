from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import PrescriptionForm
from accounts.models import User
from .models import Prescription
import datetime
from accounts.forms import NewUserForm
from django.contrib import messages
@login_required(login_url="/../accounts/login")
def doctor_dashboard(request):
    username = request.user.username

    if request.user.is_doctor:
        return render(request,"doctor/doctor_dashboard.html",{"username":username})
    else:
        return redirect("patient:patient_dashboard")

@login_required(login_url="/../accounts/login")
def prescribe(request):

    if request.user.is_doctor:
        if request.method == "POST":
            form = PrescriptionForm(request.POST)

            patient = request.POST.get("patient")
            if len(User.objects.filter(phone=patient))==1:
                try:
                    patient_user = User.objects.get(phone=patient)
                    doctor = request.user
                    date = datetime.datetime.now()
                    symptoms = request.POST.get("symptoms")
                    tests_given = request.POST.get("tests_given")
                    treatment = request.POST.get("treatment")
                    follow_up_date = request.POST.get("follow_up_date")
                    prescription = Prescription(patient=patient_user,doctor=doctor,date=date,symptoms=symptoms,tests_given=tests_given,treatment=treatment,follow_up_date=follow_up_date)
                    prescription.save()
                except:
                    return HttpResponse("Sorry! Something went wrong!")

            else:
                return redirect("doctor:patient_not_found")
        else:
            form = PrescriptionForm()
        return render(request,"doctor/prescribe.html",{"form":form})
    else:
        return redirect("patient:patient_dashboard")

@login_required(login_url="/../accounts/login")
def patient_not_found(request):
    if request.user.is_doctor:
        if request.method == "POST":
            form = NewUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                return redirect("doctor:prescribe")
        messages.error(request, "Unsuccessful registration. Invalid information.")
        form = NewUserForm()
        return render(request,"doctor/patient_not_found.html",{"register_form":form})
    else:
        return redirect("patient:patient_dashboard")


@login_required(login_url="/../accounts/login")
def previous_prescription(request):
    if request.user.is_doctor:
        entries = Prescription.objects.filter(doctor= request.user)
        print(entries)
        return render(request,"doctor/previous_prescriptions.html",{"entries":entries})
    else:
        return redirect("patient:patient_dashboard")

@login_required(login_url="/../accounts/login")
def previous_prescriptions_details(request,id):
    if request.user.is_doctor:
        entry = Prescription.objects.get(id=id)

        return render(request,"doctor/previous_prescriptions_details.html",{"entry":entry})
    
    else:

        entry = Prescription.objects.get(id=id)
        if entry.patient == request.user:
            return render(request,"doctor/previous_prescriptions_details.html",{"entry":entry})
        else:
            return redirect("patient:patient_dashboard")