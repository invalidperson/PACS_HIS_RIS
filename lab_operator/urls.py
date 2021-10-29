
from django.urls import path
from .views import labop_dashboard

app_name = "lab_operator"
urlpatterns = [
    path("dashboard",labop_dashboard,name="labop_dashboard")
]


