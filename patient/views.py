from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/../accounts/login")
def patient_dashboard(request):
    username = request.user.username
    return render(request,"patient/dashboard.html",{"username":username})