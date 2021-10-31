from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

@login_required(login_url="/../accounts/login")
def doctor_dashboard(request):
    username = request.user.username

    if request.user.is_doctor:
        return render(request,"doctor/doctor_dashboard.html",{"username":username})
    else:
        return redirect("patient:patient_dashboard")