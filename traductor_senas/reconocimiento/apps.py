"""Configuración del módulo de reconocimiento."""
from django.apps import AppConfig


class ReconocimientoConfig(AppConfig):
    """Define el nombre y comportamiento base de la app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "reconocimiento"
