"""Servicios para interactuar con OpenAI y convertir señas en voz."""
import base64
from pathlib import Path

from django.conf import settings
from openai import OpenAI


def convertir_imagen_a_base64(ruta_imagen: Path) -> str:
    """Convierte una imagen local a texto base64 para enviarla al modelo multimodal."""
    contenido_binario = ruta_imagen.read_bytes()
    return base64.b64encode(contenido_binario).decode("utf-8")


def obtener_texto_desde_sena(ruta_imagen: Path) -> str:
    """Solicita a OpenAI una descripción del significado de la seña contenida en la imagen."""
    if not settings.API_KEY_OPENAI:
        return "No hay API key configurada. Define OPENAI_API_KEY para habilitar la traducción real."

    cliente_openai = OpenAI(api_key=settings.API_KEY_OPENAI)
    imagen_base64 = convertir_imagen_a_base64(ruta_imagen)

    respuesta = cliente_openai.responses.create(
        model=settings.MODELO_VISION_OPENAI,
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": (
                            "Analiza la imagen de lengua de señas y devuelve una frase corta en español "
                            "que represente el significado más probable. Si hay duda, explica brevemente."
                        ),
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{imagen_base64}",
                    },
                ],
            }
        ],
    )

    return respuesta.output_text.strip()


def sintetizar_texto_a_voz(texto_traducido: str, ruta_audio_salida: Path) -> Path | None:
    """Genera un archivo de audio MP3 con la traducción textual usando OpenAI TTS."""
    if not settings.API_KEY_OPENAI:
        return None

    cliente_openai = OpenAI(api_key=settings.API_KEY_OPENAI)
    respuesta_audio = cliente_openai.audio.speech.create(
        model=settings.MODELO_AUDIO_OPENAI,
        voice="alloy",
        input=texto_traducido,
        format="mp3",
    )

    ruta_audio_salida.parent.mkdir(parents=True, exist_ok=True)
    with open(ruta_audio_salida, "wb") as archivo_audio:
        archivo_audio.write(respuesta_audio.read())

    return ruta_audio_salida
