from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import UploadEntryForm
from accounts.models import User
from .models import Radiological_Data
import datetime
from django.contrib import messages
import mimetypes
import os

@login_required(login_url="/../accounts/login")
def labop_dashboard(request):
    username = request.user.username

    if request.user.is_labop:
        return render(request,"lab_operator/dashboard.html",{"username":username})
    else:
        return HttpResponse("You are not allowed to see this page!")



@login_required(login_url="/../accounts/login")
def upload_entry(request):

    if request.user.is_labop:
        if request.method == "POST":
            form = UploadEntryForm(request.POST,request.FILES)

            if form.is_valid:
                
                patient = request.POST.get("patient")
                patient = User.objects.get(phone=patient)
                operator = request.user
                experiment_name = request.POST.get("experiment_name")
                patient_history = request.POST.get("patient_history")
                procedure = request.POST.get("procedure")
                findings = request.POST.get("findings")
                impression = request.POST.get("impression")
                file = request.FILES["file"]

                radiological_data = Radiological_Data(patient=patient,operator=operator,experiment_name=experiment_name,patient_history=patient_history,procedure=procedure,findings=findings,impression=impression,file=file)

                radiological_data.save()

            else:
                return redirect("doctor:patient_not_found")
        else:
            form = UploadEntryForm()
        return render(request,"lab_operator/upload_new.html",{"form":form})
    else:
        return redirect("patient:patient_dashboard")



@login_required(login_url="/../accounts/login")
def previous_entries(request):
    if request.user.is_labop:
        print("I'm here")
        print(request.user)
        entries = Radiological_Data.objects.filter(operator= request.user)
        print(entries)
        return render(request,"lab_operator/previous_uploads.html",{"entries":entries})
    else:
        print("I'm there")
        return redirect("patient:patient_dashboard")



@login_required(login_url="/../accounts/login")
def previous_entry_details(request,id):
    if request.user.is_labop:
        entry = Radiological_Data.objects.get(id=id)

        download_path =  "media/" + str(entry.file)

        return render(request,"lab_operator/previous_upload_details.html",{"entry":entry,"download_path":download_path})
    else:
        entry = Radiological_Data.objects.get(id=id)

        if entry.patient == request.user:
            
            download_path =  "media/" + str(entry.file)

            return render(request,"lab_operator/previous_upload_details.html",{"entry":entry,"download_path":download_path})
        else:
            return redirect("patient:patient_dashboard")
