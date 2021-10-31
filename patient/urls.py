
from django.urls import path
from .views import patient_dashboard
from django.contrib import admin

admin.site.site_header = "PACS HIS RIS Admin"
admin.site.site_title = "PACS HIS RIS Admin Portal"
admin.site.index_title = "Welcome to PACS HIS RIS Admin Portal"

app_name = "patient"
urlpatterns = [
    path("dashboard",patient_dashboard,name="patient_dashboard")
]


