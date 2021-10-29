from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def test_view(request):
    return render(request,"index.html")
