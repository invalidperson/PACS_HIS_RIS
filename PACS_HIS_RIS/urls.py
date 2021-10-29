from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("home_app.urls")),
    path("accounts/",include("accounts.urls")),
    path("patient/",include("patient.urls")),
    path("lab_operator/",include("lab_operator.urls")),
    path("doctor/",include("doctor.urls")),
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
