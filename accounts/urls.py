from django.urls import path,include
from .views import register_request,login_request
app_name = "accounts"
urlpatterns = [
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
]

