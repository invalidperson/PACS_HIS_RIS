
from django.urls import path
from .views import doctor_dashboard,prescribe,patient_not_found,previous_prescription,previous_prescriptions_details

app_name = "doctor"
urlpatterns = [
    path("dashboard",doctor_dashboard,name="doctor_dashboard"),
    path("prescribe",prescribe,name="prescribe"),
    path("patient_not_found",patient_not_found,name="patient_not_found"),
    path("previuos_prescriptions",previous_prescription,name="previous_prescription"),
    path("previuos_prescriptions_details/<int:id>",previous_prescriptions_details,name="previous_prescriptions_details"),
]


