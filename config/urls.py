
from django.contrib import admin
from django.urls import path, include
from artlog import views as artlog_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", artlog_views.index, name="home"),
    path("gallery/", include("artlog.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
