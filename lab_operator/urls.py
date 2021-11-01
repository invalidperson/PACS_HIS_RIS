
from django.urls import path
from .views import labop_dashboard,upload_entry,previous_entries,previous_entry_details

app_name = "lab_operator"
urlpatterns = [
    path("dashboard",labop_dashboard,name="labop_dashboard"),
    path("upload_new",upload_entry,name="new_upload"),
    path("previous_entries",previous_entries,name="previous_entries"),
    path("previous_entry_details/<int:id>",previous_entry_details,name="previous_entry_details"),
]


