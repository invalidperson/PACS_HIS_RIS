
from django.urls import path
from .views import patient_dashboard,patient_records,patient_rad_records
from django.contrib import admin



app_name = "patient"
urlpatterns = [
    path("dashboard",patient_dashboard,name="patient_dashboard"),
    path("patient_records",patient_records,name="patient_records"),
    path("patient_rad_records",patient_rad_records,name="patient_rad_records"),
]


