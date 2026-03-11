"""Rutas de la app reconocimiento."""
from django.urls import path

from .views import vista_inicio

urlpatterns = [
    path("", vista_inicio, name="inicio"),
]
