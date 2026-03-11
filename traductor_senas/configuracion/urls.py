"""Rutas principales del proyecto."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("reconocimiento.urls")),
]

if settings.MODO_DEPURACION:
    urlpatterns += static(settings.URL_MEDIA, document_root=settings.RAIZ_MEDIA)
