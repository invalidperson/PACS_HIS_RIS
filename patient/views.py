from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/../accounts/login")
def dashboard_view(request):
    username = request.user.username
    return render(request,"dashboard.html",{"username":username})