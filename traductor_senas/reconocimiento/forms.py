"""Formularios para cargar imágenes de señas."""
from django import forms


class FormularioSeña(forms.Form):
    """Permite al usuario cargar una imagen para analizar señas."""

    imagen_sena = forms.ImageField(
        label="Imagen de la seña",
        help_text="Sube una foto clara de la mano o gesto que quieras traducir.",
    )
