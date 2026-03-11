"""Vistas de la demo de traducción de señas a voz."""
from pathlib import Path
from uuid import uuid4

from django.conf import settings
from django.shortcuts import render

from .forms import FormularioSeña
from .servicios import obtener_texto_desde_sena, sintetizar_texto_a_voz


def _guardar_imagen_temporal(archivo_subido) -> Path:
    """Guarda la imagen recibida en disco para que OpenAI pueda procesarla."""
    ruta_carpeta_temporal = Path(settings.RAIZ_MEDIA) / "entradas"
    ruta_carpeta_temporal.mkdir(parents=True, exist_ok=True)

    extension_archivo = Path(archivo_subido.name).suffix or ".jpg"
    nombre_archivo = f"sena_{uuid4().hex}{extension_archivo}"
    ruta_destino = ruta_carpeta_temporal / nombre_archivo

    with open(ruta_destino, "wb+") as archivo_destino:
        for bloque_archivo in archivo_subido.chunks():
            archivo_destino.write(bloque_archivo)

    return ruta_destino


def vista_inicio(request):
    """Muestra el formulario y procesa la traducción de imagen de señas a audio."""
    formulario_sena = FormularioSeña()
    texto_traducido = ""
    url_audio_generado = ""

    if request.method == "POST":
        formulario_sena = FormularioSeña(request.POST, request.FILES)
        if formulario_sena.is_valid():
            imagen_sena = formulario_sena.cleaned_data["imagen_sena"]
            ruta_imagen = _guardar_imagen_temporal(imagen_sena)
            texto_traducido = obtener_texto_desde_sena(ruta_imagen)

            ruta_audio = Path(settings.RAIZ_MEDIA) / "audios" / f"audio_{uuid4().hex}.mp3"
            resultado_audio = sintetizar_texto_a_voz(texto_traducido, ruta_audio)
            if resultado_audio:
                url_audio_generado = f"{settings.URL_MEDIA}audios/{resultado_audio.name}"

    contexto_pagina = {
        "formulario_sena": formulario_sena,
        "texto_traducido": texto_traducido,
        "url_audio_generado": url_audio_generado,
    }
    return render(request, "reconocimiento/inicio.html", contexto_pagina)
