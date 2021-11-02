from django.urls import path,include
from .views import register_request,login_request,logout_request,account_nav
app_name = "accounts"
urlpatterns = [
    path("register", register_request, name="register"),
    path("login", login_request, name="login"),
    path("account_nav", account_nav, name="account_nav"),
    path("logout", logout_request, name="logout"),
]

