from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required(login_url="/../accounts/login")
def labop_dashboard(request):
    username = request.user.username

    if request.user.is_labop:
        return render(request,"lab_operator/dashboard.html",{"username":username})
    else:
        return HttpResponse("You are not allowed to see this page!")