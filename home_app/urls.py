
from django.urls import path
from .views import test_view

app_name = "home_app"
urlpatterns = [
    path("",test_view,name="home")
]


