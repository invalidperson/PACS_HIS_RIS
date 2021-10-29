from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/../accounts/login")
def labop_dashboard(request):
    username = request.user.username
    return render(request,"lab_operator/dashboard.html",{"username":username})