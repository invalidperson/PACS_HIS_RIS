from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/../accounts/login")
def doctor_dashboard(request):
    username = request.user.username
    return render(request,"doctor/doctor_dashboard.html",{"username":username})