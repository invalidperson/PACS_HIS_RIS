
from django.urls import path
from .views import dashboard_view

app_name = "patient"
urlpatterns = [
    path("dashboard",dashboard_view,name="patient_dashboard")
]


