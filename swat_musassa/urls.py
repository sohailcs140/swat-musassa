from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import DashboardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("core/", include("core.urls")),
    path("app/", include("app.urls")),
    path("accounts/", include("users.urls")),
    path("", DashboardView.as_view(), name="dashboard")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

